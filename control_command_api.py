import configparser
import time

from dll_api import *

# Axis number: 1
axis_num = 1
# Serial port, default 0
com_port = 0

# Minimum angle
min_angle = 0
# Maximum angle
max_angle = 365
# Axis pulse count
axis_pulses_value = 50000

config_file_path = 'dll/config.ini'
config = configparser.ConfigParser()


def get_current_angle():
    config.read(config_file_path)
    init_angle = float(config.get('Settings', 'initial_angle'))
    current_pulses = get_axis_pulses(axis_num)
    if not current_pulses:
        return None
    current_angle = round(current_pulses / axis_pulses_value * 360 + init_angle, 2)
    return current_angle


def set_axis_angle(initial_angle, target_angle):
    """

    :param initial_angle: initial angle
    :param target_angle: target angle
    :return:
    """
    set_init_angle(initial_angle)
    move_pulses = round((target_angle - initial_angle) / 360 * axis_pulses_value)
    set_axis_pulses_zero(axis_num)
    time.sleep(0.3)
    move_axis_pulses(axis_num, move_pulses)


def set_init_angle(initial_angle):
    config = configparser.ConfigParser()

    # Read configuration file
    config.read(config_file_path)

    # Check and add Settings section (if it does not exist)
    if not config.has_section('Settings'):
        config.add_section('Settings')

    # Set initial_angle value
    config.set('Settings', 'initial_angle', str(initial_angle))

    # Save the modified configuration file
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)


def set_velocity(velocity):
    """

    :param velocity: velocity
    :return:
    """
    set_axis_velocity(axis_num, velocity)


