from nes.cpu.cycle import Cycle
from nes.cpu.operations import IncrementOperation, ReadOperation
from nes.memory import AbsoluteAddress
from .instruction import Instruction


class IndirectAbsoluteInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IAL'), IncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IAH'), IncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('IAH', 'IAL'), 'ADL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('IAH', 'IAL + 1'), 'ADH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 3
