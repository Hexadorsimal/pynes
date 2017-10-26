from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read, AddressBusSelect, Move
from .addressing_mode import AddressingMode


class AbsoluteXAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddressBusSelect('PCX'), Read(), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'BAL'), AddressBusSelect('PCX'), Read(), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'BAH'), AddressBusSelect('BAX'), Read(), Increment('BAH')]))

        # When C = 1
        self.cycles.append(Cycle([AddressBusSelect('BAX'), Read()]))

    @property
    def size(self):
        return 3
