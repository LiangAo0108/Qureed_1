"""
Ideal Single Photon Source
"""
from quasi.devices.generic_device import GenericDevice
from quasi.devices.generic_device import wait_input_compute
from quasi.devices.generic_device import ensure_output_compute
from quasi.devices.port import Port
from quasi.extra import Reference
from quasi.signals import GenericQuantumSignal


_SINGLE_PHOTON_SOURCE_BIB = {
    "title":"{\"u}ber eine verbesserung der wienschen spektralgleichung",
    "author":"Planck, Max",
    "year":"1978",
    "publisher":"Springer"
}

_SINGLE_PHOTON_SOURCE_DOI = "10.1007/978-3-663-13885-3_15"

class IdealSinglePhotonSource(GenericDevice):
    """
    Ideal Single Photon Emitter
    """
    ports = {
        "OUT": Port(label="A", direction="output",signal=None,
                  signal_type=GenericQuantumSignal, device=None),
    }
    
    reference = Reference(doi=_SINGLE_PHOTON_SOURCE_DOI, bib_dict=_SINGLE_PHOTON_SOURCE_BIB)
    power_average = 1
    power_peak = 1

    def __init__(self, wavelength=1550, name=None):
        super().__init__(name)
        self.wavelength = wavelength

    @ensure_output_compute
    @wait_input_compute
    def compute_outputs(self):
        """
        Waits for the input singlas to be computed
        and then the outputs are computed by this method
        """
        pass
