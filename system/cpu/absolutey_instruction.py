from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation


class AbsoluteYInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'BAL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'BAH'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('BAH', 'BAL + Y', 'DL')]))

        # When C = 1
        self.cycles.append(Cycle([ReadOperation('BAH + 1', 'BAL + Y', 'DL')]))

    @property
    def size(self):
        return 3
