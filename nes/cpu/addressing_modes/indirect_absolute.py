from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read
from nes.memory import AbsoluteAddress
from .addressing_mode import AddressingMode


class IndirectAbsoluteAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IAL'), Increment('PCL')]))
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IAH'), Increment('PCL')]))
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('IAH', 'IAL'), 'ADL')]))
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('IAH', 'IAL + 1'), 'ADH')]))
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 3
