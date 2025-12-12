# -*- coding: utf-8 -*-
"""
Este módulo contiene la configuración de los registros Modbus
para el generador DSE73xx MKII.
"""

REGISTERS_CONFIG = (
    # --- SECCIÓN 1: REGISTROS DE 16 BITS ---
    {
        "name": "PRESIÓN_ACEITE", "address": 1024, "scale": 1, 
        "signed": False, "unit": "kPa", "size": 16
    },
    {
        "name": "TEMPERATURA_REFRIGERANTE", "address": 1025, "scale": 1,
        "signed": True, "unit": "°C", "size": 16
    },
    {
        "name": "TEMPERATURA_ACEITE", "address": 1026, "scale": 1,
        "signed": True, "unit": "°C", "size": 16
    },
    {
        "name": "NIVEL_COMBUSTIBLE", "address": 1027, "scale": 1,
        "signed": False, "unit": "%", "size": 16
    },
    {
        "name": "VOLTAJE_ALTERNADOR_CARGA", "address": 1028, "scale": 0.1,
        "signed": False, "unit": "V", "size": 16
    },
    {
        "name": "VOLTAJE_BATERIA", "address": 1029, "scale": 0.1,
        "signed": False, "unit": "V", "size": 16
    },
    {
        "name": "RPM_MOTOR", "address": 1030, "scale": 1,
        "signed": False, "unit": "RPM", "size": 16
    },
    {
        "name": "FRECUENCIA_GENERADOR", "address": 1031, "scale": 0.1,
        "signed": False, "unit": "Hz", "size": 16
    },

    # --- SECCIÓN 2: REGISTROS DE 32 BITS ---
    # Voltajes de Línea a Neutro
    {
        "name": "VOLTAJE_GEN_L1N", "address": 1032, "scale": 0.1,
        "signed": False, "unit": "V", "size": 32
    },
    {
        "name": "VOLTAJE_GEN_L2N", "address": 1034, "scale": 0.1,
        "signed": False, "unit": "V", "size": 32
    },
    {
        "name": "VOLTAJE_GEN_L3N", "address": 1036, "scale": 0.1,
        "signed": False, "unit": "V", "size": 32
    },
    # Voltajes de Línea a Línea
    {
        "name": "VOLTAJE_GEN_L1L2", "address": 1038, "scale": 0.1,
        "signed": False, "unit": "V", "size": 32
    },
    {
        "name": "VOLTAJE_GEN_L2L3", "address": 1040, "scale": 0.1,
        "signed": False, "unit": "V", "size": 32
    },
    {
        "name": "VOLTAJE_GEN_L3L1", "address": 1042, "scale": 0.1,
        "signed": False, "unit": "V", "size": 32
    },
    # Corrientes de Generador
    {
        "name": "CORRIENTE_GEN_L1", "address": 1044, "scale": 0.1,
        "signed": False, "unit": "A", "size": 32
    },
    {
        "name": "CORRIENTE_GEN_L2", "address": 1046, "scale": 0.1,
        "signed": False, "unit": "A", "size": 32
    },
    {
        "name": "CORRIENTE_GEN_L3", "address": 1048, "scale": 0.1,
        "signed": False, "unit": "A", "size": 32
    },

    # --- SECCIÓN 3: REGISTROS ACUMULADOS DE 32 BITS ---
    {
        "name": "TIEMPO_FUNCIONAMIENTO_MOTOR", "address": 1798, "scale": 1,
        "signed": False, "unit": "Segundos", "size": 32
    },
    {
        "name": "NUMERO_ARRANQUES", "address": 1802, "scale": 1,
        "signed": False, "unit": "Conteo", "size": 32
    },
    {
        "name": "TIEMPO_HASTA_SERVICE", "address": 1804, "scale": 1,
        "signed": False, "unit": "Segundos", "size": 32
    },
    {
        "name": "KW_HORAS_ACUMULADAS", "address": 1800, "scale": 0.1,
        "signed": False, "unit": "kWh", "size": 32
    },
    {
        "name": "KVA_HORAS_ACUMULADAS", "address": 1806, "scale": 0.1,
        "signed": False, "unit": "kVAh", "size": 32
    },
    {
        "name": "KVAR_HORAS_ACUMULADAS", "address": 1808, "scale": 0.1,
        "signed": False, "unit": "kVARh", "size": 32
    },
    
    # Potencia Instantánea
    {
        "name": "POTENCIA_TOTAL_KW", "address": 1540, "scale": 0.1,
        "signed": True, "unit": "kW", "size": 32
    },
    {
        "name": "POTENCIA_TOTAL_KVA", "address": 1542, "scale": 0.1,
        "signed": False, "unit": "kVA", "size": 32
    },
)
