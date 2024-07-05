from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException

def read_modbus_registers(port_name):
    """
    Reads the first 20 Modbus holding registers from the device.

    :param str port_name: The name of the serial port
    :return: A list of register values if successful, None otherwise
    :rtype: list
    """
    client = ModbusSerialClient(method="rtu", port=port_name, baudrate=9600, timeout=1)
    if not client.connect():
        print("Failed to connect to the Modbus device.")
        return None
    try:
        result = client.read_holding_registers(2, 41, 170)
        if result.isError():
            print("Failed to read Modbus registers.")
            return None
        return result.registers
    except (ModbusException, PermissionError, Exception) as e:
        print(f"Error reading Modbus registers: {e}")
        return None
    finally:
        client.close()