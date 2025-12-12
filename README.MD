# Gemini Code Assistant Context

## Project Overview

This project consists of a Python script designed to monitor a DSE73xx MKII series generator. It uses the Modbus RTU protocol to communicate with the generator over a serial connection, read various operational parameters, process the data, and send it to an external API for monitoring and storage.

The core logic is contained in `modbus_api.py`, which periodically reads data based on a structured configuration defined in `registers.py`.

### Key Technologies
- **Language:** Python 3
- **Core Libraries:**
  - `pymodbus`: For Modbus RTU communication.
  - `pyserial`: For serial port communication.
  - `requests`: For sending data to a web API.
- **Device:** DSE73xx MKII Generator Controller

## File Structure

- `modbus_api.py`: The main executable script. It handles Modbus connection, data reading, data processing, and API communication.
- `registers.py`: Contains the `REGISTERS_CONFIG` data structure. This tuple defines all the Modbus registers to be read, including their address, size (16/32-bit), data type (signed/unsigned), scaling factor, and unit.
- `requirements.txt`: Lists the Python dependencies for the project.
- `.gitignore`: Specifies files and directories ignored by Git, such as the virtual environment directory (`env/`) and build artifacts.

## Running the Application

For development, the project can be run directly as a Python script. A build process can also be used to create a standalone executable (e.g., using PyInstaller), as indicated by the presence of build-related files in `.gitignore`.

### 1. Setup Virtual Environment

The project's virtual environment folder (`env/`) is not tracked by Git. You must create and activate your own virtual environment.

**Example using `venv`:**
```sh
# Create the virtual environment
python -m venv env

# Activate the environment
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### 2. Install Dependencies

Once the virtual environment is activated, install the required Python packages using pip:
```sh
pip install -r requirements.txt
```

### 3. Configuration

Before running, you may need to configure the following constants inside `modbus_api.py`:

- `PORT_SERIAL`: The serial port your Modbus device is connected to (e.g., `COM3` on Windows, `/dev/ttyUSB0` on Linux).
- `BAUDRATE`: The communication speed (defaults to `19200`).
- `SLAVE_ADDRESS`: The Modbus slave ID of the generator (defaults to `10`).
- `API_ENDPOINT`: The URL of the external API where data will be sent.
- `READ_INTERVAL_SECONDS`: The time to wait between readings (defaults to `2`).

### 4. Running the Script

Once the dependencies are installed and the configuration is set, run the main script:

```sh
python modbus_api.py
```

The script will start running, connect to the generator, and begin sending data to the specified API endpoint. You can stop it with `Ctrl+C`.

## Development Conventions

- The primary register configuration is maintained in the `REGISTERS_CONFIG` tuple in `registers.py`.
- The script uses basic print statements for logging connection status, errors, and successfully read values.