from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move, Read, Increment, AddressBusSelect
from .addressing_mode import AddressingMode


class ZeroPageAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddressBusSelect('PCX'), Read(), Increment('PCL')]))
        self.cycles.append(Cycle([AddressBusSelect('AD_ZERO'), Move('DL', 'ADL'), Read()]))

    @property
    def size(self):
        return 2
