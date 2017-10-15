from ..cycle import Cycle
from ..operation import IncrementOperation, DecrementOperation, ReadOperation, WriteOperation
from ..implied_instruction import ImpliedInstruction


class Php(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'IR')]))
        self.cycles.append(Cycle([WriteOperation(0x01, 'S', 'P'), DecrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'IR'), IncrementOperation('PCL', 'PCH')]))

    @property
    def name(self):
        return 'PHP'

    @property
    def opcode(self):
        return 0x08

    @property
    def description(self):
        return 'Push Processor Status on Stack'
