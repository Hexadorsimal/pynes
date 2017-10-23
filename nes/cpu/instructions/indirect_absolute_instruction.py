from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import IncrementMicroinstruction, ReadMicroinstruction
from nes.memory import AbsoluteAddress
from .instruction import Instruction


class IndirectAbsoluteInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IAL'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IAH'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('IAH', 'IAL'), 'ADL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('IAH', 'IAL + 1'), 'ADH')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 3
