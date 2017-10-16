from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation


class IndirectAbsoluteInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'IAL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'IAH'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('IAH', 'IAL', 'ADL')]))
        self.cycles.append(Cycle([ReadOperation('IAH', 'IAL + 1', 'ADH')]))
        self.cycles.append(Cycle([ReadOperation('ADH', 'ADL', 'DL')]))

    @property
    def size(self):
        return 3
