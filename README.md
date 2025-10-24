WJ Rotator Motor Driver
QCoDeS framework driver for low temperature rotator probe measurements in physics experiments.

Overview
This package provides a Python driver for controlling WJ Rotator Motor systems using the QCoDeS measurement framework. It enables precise angular control of rotator probes for low-temperature physics measurements.

Prerequisites
Python 3.6+

QCoDeS Framework
Installation
Install QCoDeS:

bash
pip install qcodes
Clone or download this repository and place it in your QCoDeS contrib drivers directory:

bash
QCoDeS/
└── qcodes_contrib_drivers/
    └── drivers/
        └── WJ_Rotator/
            ├── __init__.py
            ├── WJRotator.py
            ├── dll_api.py
            ├── control_command_api.py
            └── dll/
                ├── config.ini
                ├── WJ_API.dll
                ├── WJ_API2.dll
                ├── WJ_API.h
                ├── WJ_API.cs
                └── WJ_API2.lib
File Structure
text
WJ_Rotator/
├── __init__.py
├── WJRotator.py              # Main driver class
├── dll_api.py               # DLL interface layer
├── control_command_api.py   # Command API implementation
└── dll/
    ├── config.ini           # Configuration file
    ├── WJ_API.dll           # Primary DLL library
    ├── WJ_API2.dll          # Secondary DLL library  
    ├── WJ_API.h             # C header file
    ├── WJ_API.cs            # C# interface
    └── WJ_API2.lib          # Library file
Quick Start
python
# Import the driver
from qcodes_contrib_drivers.drivers.WJ_Rotator.WJRotator import WJRotator

# Initialize the rotator
rot = WJRotator("rotator")

# Connect to the device (default COM port 4)
rot.connect()

# Configure rotation parameters
rot.initial_angle(80)    # Set initial angle
rot.final_angle(100)     # Set final angle  
rot.velocity(1)          # Set rotation velocity
rot.set_velocity_value() # Apply velocity settings

# Perform rotation
rot.rotate()

# Get current angle
current_angle = rot.get_angle()

# Close connection
rot.close()
API Reference
Core Methods
connect(port=4) - Establish connection to rotator (default COM port 4)

initial_angle(value) - Set initial angle (degrees)

final_angle(value) - Set final angle (degrees)

velocity(value) - Set rotation velocity

set_velocity_value() - Apply velocity configuration

rotate() - Execute rotation

get_angle() - Read current angle

close() - Close connection and release resources

Default Values
Initial Angle: 0°

Final Angle: 360°

Velocity: 1

COM Port: 4

