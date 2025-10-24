
# WJ_Rotator_Motor
The following is the QCODES Framework driver files for using low temperature rotator probe to perform low temperatures physics measurements.

# How to setup 
1) Install QCODES in Python from following link (https://microsoft.github.io/Qcodes/)
2) Download all files from here and make folder workflow like below:-
```bash
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
```
3) Open the qcodes folder that you downloaded and go to qcodes_contrib_drivers and paste the folder that you made in step 2

# Usage Commands

#Rotator Probe
 
1) from qcodes_contrib_drivers.drivers.WJRotator import WJRotator #importing the driver
2) rot=WJRotator("rotator") #give a variable name to WJRotator class and model name ,could be any name "in brackets"
3) rot.connect() #connecting the rotator to port and establishing the connection, default port=4 so always insert in that port otherwise change the default port in code according to your 4) convenience
5) rot.initial_angle(80) #giving value to initial angle, initial value=0 but rotator at start can be at any angle so set accordingly
6) rot.final_angle(100)  #giving value to final angle, initial value=360 
7) rot.velocity(1) #giving value to velocity, initial value=1
8) rot.set_velocity_value() #setting the velocity value
9) rot.rotate() #for rotating the probe
10) rot.get_angle() #for getting current angle
11) rot.close() #run this to close com port connection first and then remove the cable

