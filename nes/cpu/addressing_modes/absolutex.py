from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, RW, AddressBus, Move
from .addressing_mode import AddressingMode


class AbsoluteXAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'BAL'), AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'BAH'), AddressBus('BAX'), RW(1), Increment('BAH')]))

        # When C = 1
        self.cycles.append(Cycle([AddressBus('BAX'), RW(1)]))

    @property
    def size(self):
        return 3
