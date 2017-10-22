from .alu.alu import AluIncrementOperation
from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation
from ..memory.address import AbsoluteAddress


class IndirectAbsoluteInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IAL'), AluIncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IAH'), AluIncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('IAH', 'IAL'), 'ADL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('IAH', 'IAL + 1'), 'ADH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 3
