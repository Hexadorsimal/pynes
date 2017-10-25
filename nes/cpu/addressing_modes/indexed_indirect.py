from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import IncrementMicroinstruction, ReadMicroinstruction
from nes.memory import AbsoluteAddress, ZeroPageAddress
from .addressing_mode import AddressingMode


class IndexedIndirectAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'BAL'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(ZeroPageAddress('BAL'), 'DL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(ZeroPageAddress('BAL + X'), 'ADL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(ZeroPageAddress('BAL + X + 1'), 'ADH')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 2
