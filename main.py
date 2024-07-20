from ascii_art import display_v
import serial
from modbus_utils import read_modbus_registers
from serial_utils import list_serial_ports, print_serial_ports, choose_serial_port
from transform_utils import transform_and_rename_registers, REGISTER_NAMES, UNITS
import time

def read_from_serial(port_name: str):
    """
    Reads data from the selected serial port.

    :param str port_name: The name of the serial port
    """
    try:
        with serial.Serial(port_name, 9600, timeout=1) as ser:
            print(f"Connected to {port_name}.\n \nBridge the DET and TEST pins")
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode("utf-8").rstrip()
                    if line:
                        print(line)
                        print()
                        time.sleep(2)
                        break
        raw_registers = read_modbus_registers(port_name)
        if raw_registers:
            transformed_data = transform_and_rename_registers(raw_registers)
            for k in REGISTER_NAMES:
                value = transformed_data[k]
                unit = UNITS[k]
                print(f"{REGISTER_NAMES[k]} {value} {unit}")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"Serial exception error: {e}")


def main():
    """
    Main function to list serial ports, choose a port, and read data from it.
    """
    display_v(6)
    print("VB Tool v1.0.0")
    print()
    ports = list_serial_ports()
    if not ports:
        print("No serial ports found.")
        return
    print_serial_ports(ports)
    port_name = choose_serial_port(ports)
    read_from_serial(port_name)


if __name__ == "__main__":
    main()
