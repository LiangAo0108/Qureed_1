"""
 created with template
"""

from typing import Union
from quasi.devices import (
    GenericDevice,
    wait_input_compute,
    schedule_next_event,
    coordinate_gui,
    log_action,
    ensure_output_compute,
)

from quasi.devices.port import Port
from quasi.simulation import ModeManager
from quasi.signals import *
from quasi.gui.icons import icon_list


class PulseSorter(GenericDevice):
    ports = {
        "sort": Port(
            label="sort",
            direction="input",
            signal=None,
            signal_type=GenericBoolSignal,
            device=None,
        ),
        "input": Port(
            label="input",
            direction="input",
            signal=None,
            signal_type=GenericQuantumSignal,
            device=None,
        ),
        "pulse1": Port(
            label="pulse1",
            direction="output",  # Changed from "input" to "output" for clarity
            signal=None,
            signal_type=GenericQuantumSignal,
            device=None,
        ),
        "pulse2": Port(
            label="pulse2",
            direction="output",  # Changed from "input" to "output" for clarity
            signal=None,
            signal_type=GenericQuantumSignal,
            device=None,
        ),
    }

    gui_icon = icon_list.SORTER
    gui_tags = []
    gui_documentation = None
    gui_name = "Pulse Sorter"

    power_peak = 0
    power_average = 0

    reference = None

    @ensure_output_compute
    @coordinate_gui
    @wait_input_compute
    def compute_outputs(self, *args, **kwargs):
        """
        Implement to use the regular backend
        """
        pass

    @log_action
    @schedule_next_event
    def des(self, time, *args, **kwargs):
        """
        Implement to use discrete event simulation
        """
        pass

    @log_action
    @schedule_next_event
    def des_action(self, time=None, *args, **kwargs):
        """
        Or implement this if you are implementing a trigger
        """
        pass
