from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read
from nes.memory import AbsoluteAddress, ZeroPageAddress
from .addressing_mode import AddressingMode


class IndirectIndexedAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('PCH', 'PCL'), 'IAL'), Increment('PCL')]))
        self.cycles.append(Cycle([Read(), (ZeroPageAddress('IAL'), 'BAL')]))
        self.cycles.append(Cycle([Read(), (ZeroPageAddress('IAL + 1'), 'BAH')]))
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('BAH', 'BAL + Y'), 'DL')]))

        # when C = 1 or read-modify-write or STA
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('BAH + 1', 'BAL + Y'), 'DL')]))

    @property
    def size(self):
        return 2
