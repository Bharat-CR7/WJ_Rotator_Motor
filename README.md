# WJ Rotator Motor Driver

QCoDeS framework driver for low temperature rotator probe measurements in physics experiments.

## Overview

This package provides a Python driver for controlling WJ Rotator Motor systems using the QCoDeS measurement framework. It enables precise angular control of rotator probes for low-temperature physics measurements.

## Prerequisites

- Python 3.6+
- [QCoDeS Framework](https://microsoft.github.io/Qcodes/)

## Installation

1. Install QCoDeS:
```bash
pip install qcodes
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

