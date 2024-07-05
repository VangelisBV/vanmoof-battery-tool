import serial.tools.list_ports
import serial

def list_serial_ports():
    """
    Lists all available serial ports.

    :return: A list of available serial ports
    :rtype: list
    """
    return serial.tools.list_ports.comports()


def print_serial_ports(ports):
    """
    Prints the list of available serial ports.

    :param list ports: A list of serial ports
    """
    print("Available serial ports:")
    for idx, port in enumerate(ports):
        print(f"{idx}: {port.device} - {port.description}")
    print()


def choose_serial_port(ports):
    """
    Prompts the user to choose a serial port from the list.

    :param list ports: A list of serial ports
    :return: The device name of the chosen serial port
    :rtype: str
    """
    while True:
        try:
            index = int(input("Enter the index number of the port you want to connect to: "))
            if 0 <= index < len(ports):
                return ports[index].device
            else:
                print("Invalid index. Please choose a valid port number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
