import sys
from typing import Optional
from qcodes.instrument import Instrument
from qcodes import validators as vals

from dll_api import *
from control_command_api import *


class WJRotator(Instrument):

    DLL_FOLDER = os.path.join(os.path.dirname(__file__), "dll")
    DEFAULT_DLL_PATH = os.path.join(DLL_FOLDER, "WJ_API.dll")

    def __init__(
        self,
        name: str,
        *,
        dll_path: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(name, **kwargs)

        if sys.platform != "win32":
            raise OSError("WJRotator only works on Windows (WJ_API.dll is Windows-only).")

        self._dll_path = dll_path or self.DEFAULT_DLL_PATH

        # ---- Parameters ----
        self.add_parameter(
            "initial_angle",
            initial_value=0,  # Default until user sets explicitly
            set_cmd=None,
            vals=vals.Numbers(0, 360),
            unit="°",
            docstring="Starting angle in degrees"
        )

        self.add_parameter(
            "final_angle",
            initial_value=360,  # Default until user sets explicitly
            set_cmd=None,
            vals=vals.Numbers(0, 360),
            unit="°",
            docstring="Target angle in degrees"
        )

        self.add_parameter(
            "velocity",
            initial_value=1,
            set_cmd=None,
            vals=vals.Ints(1, 2),
            unit="°/s",
            docstring="Rotation speed (1-2)"
        )

    def connect(self):
        """Explicitly open COM connection to hardware."""
        open_res = wj_api.WJ_Open(0)
        if open_res != 0:
            raise RuntimeError(f"Failed to open COM port (error code {open_res})")

    def get_angle(self):
        """Explicitly read the current angle from hardware."""
        return get_current_angle()

    def rotate(self):
        """Move from initial_angle to final_angle at set velocity."""
        set_axis_angle(self.initial_angle(), self.final_angle())
    
    def set_velocity_value(self):
        """Send the current velocity setting to hardware."""
        set_velocity(int(self.velocity()))

    def close(self):
        """Explicitly close COM connection."""
        wj_api.WJ_Close()
        super().close()








