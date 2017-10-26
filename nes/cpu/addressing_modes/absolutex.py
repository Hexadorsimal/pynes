from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read
from nes.memory import AbsoluteAddress
from .addressing_mode import AddressingMode


class AbsoluteXAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('PCH', 'PCL'), 'BAL'), Increment('PCL')]))
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('PCH', 'PCL'), 'BAH'), Increment('PCL')]))
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('BAH', 'BAL + X'), 'DL')]))

        # When C = 1
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('BAH + 1', 'BAL + X'), 'DL')]))

    @property
    def size(self):
        return 3
