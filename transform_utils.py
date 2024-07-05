REGISTER_NAMES = {
    0: "Errors:",
    1: "Temperature:",
    2: "Voltage:",
    3: "SOC:",
    10: "ESN:",
    19: "Nominal Capacity:",
    20: "Full Charge Capacity:",
    21: "Remaining Capacity:",
    23: "Cycles:",
    25: "Cells Pack 1:",
    26: "Cells Pack 2:",
    27: "Cells Pack 3:",
    28: "Cells Pack 4:",
    29: "Cells Pack 5:",
    30: "Cells Pack 6:",
    31: "Cells Pack 7:",
    32: "Cells Pack 8:",
    33: "Cells Pack 9:",
    34: "Cells Pack 10:",
    39: "Cell Packs Max Actual:",
    40: "Cell Packs Min Actual:"
}
UNITS = {
    0: "",
    1: "",
    2: "Volt",
    3: "%",
    10: "",
    19: "mAh",
    20: "mAh",
    21: "mAh",
    23: "",
    25: "V",
    26: "V",
    27: "V",
    28: "V",
    29: "V",
    30: "V",
    31: "V",
    32: "V",
    33: "V",
    34: "V",
    39: "V",
    40: "V"
}

def transform_data(index, value):
    """
    Transforms the register data based on the index.

    :param int index: The index of the register
    :param int value: The value of the register   
    :return: The transformed value based on the index
    :rtype: float
    """
    if index == 0:
        return decode_errors(value)
    elif index in [2, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 39, 40]:
        return round(value / 1000.0, 4)
    elif index in [10, 11, 12, 13, 14, 15, 16]:
        try:
            return bytearray([value >> 8, value & 0xFF]).decode("ascii")
        except Exception as e:
            return f"Invalid ASCII value: {e}"
    elif index in [4, 5, 6, 7, 8, 9, 17, 18]:
        return None
    return value


def decode_errors(error_code):
    """
    Decodes error codes into human-readable messages.

    :param int error_code: The error code
    :return: A comma-separated string of error messages
    :rtype: str
    """
    error_messages = [
        "Short Circuit Protection", 
        "MOS Temperature Protection",
        "Pack Discharge Short Circuit Protection", 
        "Pack Discharge Over Current Protection",
        "Under Voltage Protection 2", 
        "Under Voltage Protection 1",
        "Over Voltage Protection 2", 
        "Over Voltage Protection 1",
        "Charging Over Current Protection 2", 
        "Charging Over Current Protection 1",
        "Discharging Over Current Protection 2", 
        "Discharging Over Current Protection 1",
        "Charging Under Temperature Protection", 
        "Charging Over Temperature Protection",
        "Discharging Under Temperature Protection", 
        "Discharging Over Temperature Protection",
    ]
    binary_representation = format(error_code, "016b")
    errors = [error_messages[i] for i, bit in enumerate(binary_representation) if bit == "1"]
    return ",".join(errors) if errors else "No errors"


def transform_and_rename_registers(registers):
    """
    Transforms and renames the Modbus register values.

    :param list registers: A list of register values
    :return: A dictionary of transformed and renamed register values
    :rtype: dict
    """
    transformed_data = {index: transform_data(index, value) for index, value in enumerate(registers)}
    filtered_data = {k: v for k, v in transformed_data.items() if v is not None}
    esn = "".join([filtered_data.pop(k) for k in range(10, 17) if k in filtered_data])
    filtered_data[10] = esn
    return filtered_data
