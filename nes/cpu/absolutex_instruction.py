from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation


class AbsoluteXInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'BAL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'BAH'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('BAH', 'BAL + X', 'DL')]))

        # When C = 1
        self.cycles.append(Cycle([ReadOperation('BAH + 1', 'BAL + X', 'DL')]))

    @property
    def size(self):
        return 3
