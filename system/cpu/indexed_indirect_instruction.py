from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation


class IndexedIndirectInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'BAL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(0x00, 'BAL', 'DL')]))
        self.cycles.append(Cycle([ReadOperation(0x00, 'BAL + X', 'ADL')]))
        self.cycles.append(Cycle([ReadOperation(0x00, 'BAL + X + 1', 'ADH')]))
        self.cycles.append(Cycle([ReadOperation('ADH', 'ADL', 'DL')]))

    @property
    def size(self):
        return 2
