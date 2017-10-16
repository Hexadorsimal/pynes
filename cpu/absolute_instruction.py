from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation


class AbsoluteInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'ADL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'ADH'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('ADH', 'ADL', 'DL')]))

    @property
    def size(self):
        return 3
