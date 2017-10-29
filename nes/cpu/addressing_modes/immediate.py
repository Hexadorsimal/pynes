from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, RW, AddressBus
from .addressing_mode import AddressingMode


class ImmediateAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RW(1), AddressBus('PCX'), Increment('PCL')]))

    @property
    def size(self):
        return 2
