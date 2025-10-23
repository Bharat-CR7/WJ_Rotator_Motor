import ctypes
import sys
import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory of the current file
current_directory = os.path.dirname(current_file_path)

# Add the directory of the current file to sys.path
if current_directory not in sys.path:
    sys.path.append(current_directory)

# Load DLL
dll_path = os.path.realpath('dll/WJ_API.dll')

try:
    wj_api = ctypes.CDLL(dll_path)
except OSError as e:
    print(f"Failed to load WJ_API.dll: {e}")
    sys.exit(1)

# Define function prototypes
wj_api.WJ_Open.argtypes = [ctypes.c_int]
wj_api.WJ_Open.restype = ctypes.c_int32

wj_api.WJ_Close.argtypes = []
wj_api.WJ_Close.restype = ctypes.c_int32

wj_api.WJ_Get_Axis_Status.argtypes = [ctypes.c_int32, ctypes.POINTER(ctypes.c_int32)]
wj_api.WJ_Get_Axis_Status.restype = ctypes.c_int32

# Add WJ_Get_Axis_Vel function prototype
wj_api.WJ_Get_Axis_Vel.argtypes = [ctypes.c_int32, ctypes.POINTER(ctypes.c_int32)]
wj_api.WJ_Get_Axis_Vel.restype = ctypes.c_int32

# Define WJ_Set_Axis_Vel function prototype
wj_api.WJ_Set_Axis_Vel.argtypes = [ctypes.c_int32, ctypes.c_int32]
wj_api.WJ_Set_Axis_Vel.restype = ctypes.c_int32

# Define WJ_Set_Axis_Subdivision function prototype
wj_api.WJ_Set_Axis_Subdivision.argtypes = [ctypes.c_int32, ctypes.c_int32]
wj_api.WJ_Set_Axis_Subdivision.restype = ctypes.c_int32

# Define pulse movement function prototype
wj_api.WJ_Move_Axis_Pulses.argtypes = [ctypes.c_int32, ctypes.c_int32]
wj_api.WJ_Move_Axis_Pulses.restype = ctypes.c_int32

# Define pulse movement (all axes) function prototype
wj_api.WJ_Move_Axes_Pulses.argtypes = [ctypes.POINTER(ctypes.c_int32)]
wj_api.WJ_Move_Axes_Pulses.restype = ctypes.c_int32

# Define WJ_Get_Axis_Pulses function prototype
wj_api.WJ_Get_Axis_Pulses.argtypes = [ctypes.c_int32, ctypes.POINTER(ctypes.c_int32)]
wj_api.WJ_Get_Axis_Pulses.restype = ctypes.c_int32

# Define WJ_Get_Axes_Pulses function prototype
wj_api.WJ_Get_Axes_Pulses.argtypes = [ctypes.POINTER(ctypes.c_int32)]
wj_api.WJ_Get_Axes_Pulses.restype = ctypes.c_int32

# Define WJ_Get_Axis_Subdivision function prototype
wj_api.WJ_Get_Axis_Subdivision.argtypes = [ctypes.c_int32, ctypes.POINTER(ctypes.c_int32)]
wj_api.WJ_Get_Axis_Subdivision.restype = ctypes.c_int32

# Define function prototype
wj_api.WJ_Set_Axis_Pulses_Zero.argtypes = [ctypes.c_int32]
wj_api.WJ_Set_Axis_Pulses_Zero.restype = ctypes.c_int32


# Get axis subdivision
def get_axis_subdivision(axis_num):
    p_value = ctypes.c_int32()
    # Ensure axis_num is ctypes.c_int32 type
    axis_num_c = ctypes.c_int32(axis_num)
    result = wj_api.WJ_Get_Axis_Subdivision(axis_num_c, ctypes.byref(p_value))
    if result == 0:
        print(f"WJ_Get_Axis_Subdivision: {p_value.value}")
        return p_value.value
    else:
        print(f"WJ_Get_Axis_Subdivision failed, error code: {result}")
        return 3200

def set_axis_subdivision(axis_num, value):
    result = wj_api.WJ_Set_Axis_Subdivision(axis_num, value)
    if result == 0:
        print(f"Axis {axis_num} subdivision set successfully, speed: {value}")
    else:
        print(f"Axis {axis_num} subdivision set failed, error code: {result}")


# Get status of all axes
def get_all_axes_status():
    # Get number of axes
    axes_num = ctypes.c_int32(0)
    result = wj_api.WJ_Get_Axes_Num(ctypes.byref(axes_num))
    if result != 0:
        print(f"WJ_Get_Axes_Num failed, error code: {result}")
        return

    # Get status of all axes
    axes_status = (ctypes.c_int32 * axes_num.value)()
    result = wj_api.WJ_Get_Axes_Status(axes_status)
    if result == 0:
        for i in range(axes_num.value):
            print(f"Axis {i + 1} status: {axes_status[i]}")
    else:
        print(f"WJ_Get_Axes_Status failed, error code: {result}")


# Get velocity of specified axis
def get_axis_velocity(axis_num):
    p_value = ctypes.c_int32()
    result = wj_api.WJ_Get_Axis_Vel(axis_num, ctypes.byref(p_value))
    if result == 0:
        print(f"Axis {axis_num} velocity: {p_value.value}")
        return p_value.value
    else:
        print(f"WJ_Get_Axis_Vel failed, error code: {result}")


# Emergency stop specified axis
def emergency_stop_axis(axis_num):
    result = wj_api.WJ_Move_Axis_Emergency_Stop(axis_num)
    if result == 0:
        print(f"Axis {axis_num} emergency stop successful")
    else:
        print(f"Axis {axis_num} emergency stop failed, error code: {result}")


# Set velocity of specified axis
def set_axis_velocity(axis_num, value):
    result = wj_api.WJ_Set_Axis_Vel(axis_num, value)
    if result == 0:
        print(f"Axis {axis_num} velocity set successfully, speed: {value}")
    else:
        print(f"Axis {axis_num} velocity set failed, error code: {result}")


# Move specified axis by pulse count
def move_axis_pulses(axis_num, value):
    result = wj_api.WJ_Move_Axis_Pulses(axis_num, value)
    if result == 0:
        print(f"Axis {axis_num} moved by pulse count {value} successfully")
    else:
        print(f"Axis {axis_num} moved by pulse count {value} failed, error code: {result}")


# Move multiple axes by pulse count
def move_axes_pulses(p_value_axes):
    num_axes = len(p_value_axes)
    # Create C type array type
    array_type = ctypes.c_int32 * num_axes
    # Instantiate array
    p_value_axes_array = array_type(*p_value_axes)
    result = wj_api.WJ_Move_Axes_Pulses(p_value_axes_array)
    if result == 0:
        print(f"Move multiple axes by pulse count successfully")
    else:
        print(f"Move multiple axes by pulse count failed, error code: {result}")


# Get pulse count of specified axis
def get_axis_pulses(axis_num):
    p_value = ctypes.c_int32()
    result = wj_api.WJ_Get_Axis_Pulses(axis_num, ctypes.byref(p_value))
    if result == 0:
        print(f"Axis {axis_num} pulse count: {p_value.value}")
        return p_value.value
    else:
        print(f"WJ_Get_Axis_Pulses failed, error code: {result}")
        return 0


# Get pulse count of all axes
def get_axes_pulses():
    # Get number of axes
    axes_num = ctypes.c_int32(0)
    result = wj_api.WJ_Get_Axes_Num(ctypes.byref(axes_num))
    if result != 0:
        print(f"WJ_Get_Axes_Num failed, error code: {result}")
        return

    # Get pulse count of all axes
    axes_pulses = (ctypes.c_int32 * axes_num.value)()
    result = wj_api.WJ_Get_Axes_Pulses(axes_pulses)
    if result == 0:
        for i in range(axes_num.value):
            print(f"Axis {i + 1} pulse count: {axes_pulses[i]}")
    else:
        print(f"WJ_Get_Axes_Pulses failed, error code: {result}")


def set_axis_pulses_zero(axis_num):
    """
    Call WJ_Set_Axis_Pulses_Zero function

    :param axis_num: Axis number
    :return: Return value (INT32)
    """
    return wj_api.WJ_Set_Axis_Pulses_Zero(axis_num)


if __name__ == "__main__":
    # Communication initialization
    com_port = 0  # Assume using COM0
    result = wj_api.WJ_Open(com_port)
    if result != 0:
        print(f"WJ_Open failed, error code: {result}")
        sys.exit(1)

    # move_axis_pulses(1, 136)
    # emergency_stop_axis(1)
    # Get status of all axes
    get_all_axes_status()

    # Get velocity of specified axis
    axis_num = 1  # Assume querying the speed of the 1st axis
    get_axis_velocity(axis_num)
    get_axis_subdivision(axis_num)
    # Get pulse count of specified axis
    get_axis_pulses(axis_num)

    # Get pulse count of all axes
    get_axes_pulses()

    # Close communication
    result = wj_api.WJ_Close()
    if result != 0:
        print(f"WJ_Close failed, error code: {result}")
        sys.exit(1)

    sys.exit(0)
