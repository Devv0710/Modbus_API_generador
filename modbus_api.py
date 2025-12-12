"""
Este módulo se encarga de leer datos de un generador a través de Modbus RTU,
procesarlos y enviarlos a una API externa.
"""
import time
import json
import requests
from pymodbus.client import ModbusSerialClient
from pymodbus import ModbusException

# Importar la configuración de registros
from registers import REGISTERS_CONFIG

# --- Constantes de Configuración ---
PORT_SERIAL = '/dev/ttyUSB0'
BAUDRATE = 19200
SLAVE_ADDRESS = 10
API_ENDPOINT = "https://api.example.com/generator_data"  # URL de la API externa
READ_INTERVAL_SECONDS = 2


def connect_modbus(port, baudrate):
    """
    Establece la conexión con el cliente Modbus y la devuelve.
    """
    client = ModbusSerialClient(
        port=port,
        baudrate=baudrate,
        bytesize=8,
        parity='N',
        stopbits=1,
        framer='rtu'
    )
    print("Conectando al generador...")
    if not client.connect():
        print("Error: No se pudo conectar al dispositivo Modbus.")
        return None
    print("Conexión establecida.")
    return client

def read_register_values(client, registers_config):
    """
    Lee los valores de los registros configurados desde el dispositivo Modbus,
    los decodifica y los devuelve en un diccionario.
    """
    data = {"timestamp": int(time.time())}
    print("Leyendo valores de registros...")

    for reg in registers_config:
        try:
            count = 2 if reg["size"] == 32 else 1
            response = client.read_holding_registers(
                address=reg["address"],
                count=count,
                slave=SLAVE_ADDRESS,
            )

            if response.isError():
                print(f"Error al leer el registro '{reg['name']}': {response}")
                data[reg['name']] = None
                continue

            value = 0
            if reg["size"] == 32:
                if reg["signed"]:
                    value = client.convert_from_registers(
                        registers=response.registers,
                        data_type=client.DATATYPE.INT32,
                    )
                else:
                    value = client.convert_from_registers(
                        registers=response.registers,
                        data_type=client.DATATYPE.UINT32,
                    )
            else:  # 16-bit
                if reg["signed"]:
                    value = client.convert_from_registers(
                        registers=response.registers,
                        data_type=client.DATATYPE.INT16,
                    )
                else:
                    value = client.convert_from_registers(
                        registers=response.registers,
                        data_type=client.DATATYPE.UINT16,
                    )
            
            # Aplicar el factor de escala
            scaled_value = value * reg["scale"]
            
            # Redondear a 2 decimales si el factor de escala es decimal
            if isinstance(reg["scale"], float) and reg["scale"] < 1.0:
                scaled_value = round(scaled_value, 2)

            data[reg['name']] = scaled_value
            print(f"  - {reg['name']}: {scaled_value} {reg['unit']}")

        except ModbusException as exc:
            print(f"Excepción Modbus al leer '{reg['name']}': {exc}")
            data[reg['name']] = None
        except Exception as e:
            print(f"Error inesperado al procesar el registro '{reg['name']}': {e}")
            data[reg['name']] = None
            
    return data

def send_data_to_api(data, endpoint):
    """
    Envía los datos en formato JSON a la API especificada via POST.
    """
    headers = {'Content-Type': 'application/json'}
    try:
        print(f"Enviando {len(data)} puntos de datos a {endpoint}...")
        response = requests.post(endpoint, data=json.dumps(data, indent=2), headers=headers, timeout=10)
        
        if response.status_code >= 200 and response.status_code < 300:
            print(f"Datos enviados con éxito. Respuesta: {response.status_code}")
        else:
            print(f"Error al enviar datos. Código de estado: {response.status_code}")
            print(f"Respuesta: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"No se pudo enviar los datos a la API. Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado al enviar los datos: {e}")


def main():
    """
    Función principal que orquesta la lectura de datos y el envío a la API.
    """
    print("Iniciando la aplicación de monitoreo del generador.")    
    registers_config = REGISTERS_CONFIG
    if not registers_config:
        print("Error: No se pudieron cargar los registros. Saliendo.")
        return

    client = connect_modbus(PORT_SERIAL, BAUDRATE)
    if not client:
        return

    try:
        while True:
            # 1. Leer los valores de los registros
            generator_data = read_register_values(client, registers_config)
            
            # 2. Enviar los datos a la API
            send_data_to_api(generator_data, API_ENDPOINT)
            
            # 3. Esperar el intervalo definido
            print(f"Esperando {READ_INTERVAL_SECONDS} segundos para la próxima lectura...")
            time.sleep(READ_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\nDeteniendo la aplicación.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        if client and client.is_open:
            client.close()
            print("Conexión Modbus cerrada.")

if __name__ == "__main__":
    main()