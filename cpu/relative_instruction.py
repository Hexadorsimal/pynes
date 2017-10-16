from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation


class RelativeInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'DL')]))

    @property
    def size(self):
        return 2
