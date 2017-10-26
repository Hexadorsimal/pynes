from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read, AddressBusSelect, Move
from .addressing_mode import AddressingMode


class AbsoluteAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddressBusSelect('PCX'), Read(), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'ADL'), AddressBusSelect('PCX'), Read(), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'ADH'), AddressBusSelect('ADX'), Read()]))

    @property
    def size(self):
        return 3
