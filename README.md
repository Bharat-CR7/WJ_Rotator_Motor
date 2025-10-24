⚙️ How to Setup

Install QCoDeS in Python from the official link:
👉 https://microsoft.github.io/Qcodes/

Download all files from this repository and make the folder structure as shown below:

WJ_Rotator/
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


Open the qcodes folder that you downloaded and go to
qcodes_contrib_drivers/, then paste the folder you made in step 2.
🧩 Usage Commands
Rotator Probe Example
# Import the driver
from qcodes_contrib_drivers.drivers.WJRotator import WJRotator

# Create an instance of the driver
rot = WJRotator("rotator")  # "rotator" can be any name

# Connect to the rotator (default COM port = 4)
rot.connect()

# Set up parameters
rot.initial_angle(80)    # Set initial angle (default = 0)
rot.final_angle(100)     # Set final angle (default = 360)
rot.velocity(1)          # Set velocity (default = 1)
rot.set_velocity_value() # Apply the velocity setting

# Perform rotation
rot.rotate()             # Start rotation
print(rot.get_angle())   # Get current angle

# Close the connection
rot.close()              # Always close COM port before disconnecting
