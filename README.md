# A Python Script to Read the SX3 Batteries Registers 

This Python script scans for available serial ports, prompts the user to select a port, and then reads the Modbus registers from the VM battery, which is connected via a USB to UART bridge. The script transforms and renames the Modbus register values, and then displays the results.

...

## Features

- Scans for available serial ports.
- Prompts the user to select a serial port.
- Reads Modbus holding registers from the battery.
- Transforms and renames the register values.
- Displays the transformed data. 


## Requirements

- 1x USB to UART Bridge (CP2102)
- 3x Female to male jumper wires
- 1x Male to male jumper wire
- Python 3.6 or higher
- Python virtualenv (optional)
- [PySerial] (https://github.com/pyserial/pyserial)
- [PyModbus] (https://github.com/pymodbus-dev/pymodbus)


## Installation

1. **Install Python**
If you don't have Python installed already, download and install it from the official [website](https://www.python.org/downloads/).

2. **Clone the repository:**
   ```sh
   git clone https://github.com/VangelisBV/vanmoof-battery-tool.git
   cd vanmoof-battery-tool

3. **Create a virtual environment (optional but recommended):**
       ```sh
    pip install virtualenv   
    python -m virtualenv venv
    source venv\Scripts\activate # On Linux, use: venv/bin/activate 

4. **Install the required libraries:**
       ```sh
    pip install -r requirements.txt


## Usage

1. **Connect the battery to your PC using a USB to UART bridge according to the diagram:**
<image>

2. **Run the script:**
       ```sh
    python main.py

3. **Follow the prompts to select the serial port:**
- The script will list all available serial ports.
- Enter the index number corresponding to the port your battery is connected to.

4. **"Wake up" the battery:**
The script will ask you to momentarily bridge the DET and the TEST pins of the battery:
<image>

5. **Read the results**
The register values are transformed, renamed and then the results are displayed.


## Example Output
<image>


## Contributing & Future Plans
Research to expand the tool is ongoing and contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have suggestions for improvements, bug reports, or new features.


## Acknowledgments
- [PySerial] (https://github.com/pyserial/pyserial)
- [PyModbus] (https://github.com/pymodbus-dev/pymodbus)


## Disclaimer
This software is provided "as is". The authors make no representations or warranties of any kind concerning the safety, suitability, inaccuracies or other harmful components of this software. The authors will not be liable for any damages you may suffer in connection with using, modifying, or distributing this software.
**Use this software at your own risk.** This project is intended for research purposes only. 
**Please note that register naming and transformations have been done based on my own research and no information has been provided by VM.**