from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read
from nes.memory import AbsoluteAddress, ZeroPageAddress
from .addressing_mode import AddressingMode


class IndexedIndirectAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('PCH', 'PCL'), 'BAL'), Increment('PCL')]))
        self.cycles.append(Cycle([Read(), (ZeroPageAddress('BAL'), 'DL')]))
        self.cycles.append(Cycle([Read(), (ZeroPageAddress('BAL + X'), 'ADL')]))
        self.cycles.append(Cycle([Read(), (ZeroPageAddress('BAL + X + 1'), 'ADH')]))
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 2
