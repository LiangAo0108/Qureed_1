"""
Float Variable
"""

from quasi.devices import (
    GenericDevice,
    wait_input_compute,
    coordinate_gui,
    ensure_output_compute,
    log_action,
    schedule_next_event,
)
from quasi.devices.port import Port
from quasi.signals import GenericFloatSignal

from quasi.gui.icons import icon_list


class FloatVariable(GenericDevice):
    """
    Implements integer variable setter
    """

    ports = {
        "float": Port(
            label="float",
            direction="output",
            signal=None,
            signal_type=GenericFloatSignal,
            device=None,
        ),
    }

    # Gui Configuration
    gui_icon = icon_list.SIMPLE_TRIGGER
    gui_tags = ["variable", "float"]
    gui_name = "Float Variable"
    power = 0
    power_average = 0
    power_peak = 0
    reference = None

    values = {"value": None}

    def __init__(self, name=None, uid=None):
        super().__init__(name=name, uid=uid)
        self.simulation.schedule_event(0, self)

    @ensure_output_compute
    @coordinate_gui
    @wait_input_compute
    def compute_outputs(self, *args, **kwargs):
        self.ports["float"].signal.set_float(self.values["value"])
        self.ports["float"].signal.set_computed()

    def set_value(self, value: str):
        self.values["value"] = float(value)

    @log_action
    @schedule_next_event
    def des_action(self, time=None, *args, **kwargs):
        signal = GenericFloatSignal()
        signal.set_float(self.values["value"])
        result = [("float", signal, time)]
        print(self.values["value"])
        return result
