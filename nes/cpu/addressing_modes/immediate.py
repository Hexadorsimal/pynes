from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read, AddressBusSelect
from .addressing_mode import AddressingMode


class ImmediateAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(), AddressBusSelect('PCX'), Increment('PCL')]))

    @property
    def size(self):
        return 2
