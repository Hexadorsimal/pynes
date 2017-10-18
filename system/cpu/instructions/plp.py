from ..cycle import Cycle
from ..operation import IncrementOperation, ReadOperation, WriteOperation
from ..implied_instruction import ImpliedInstruction


class Plp(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'IR')]))
        self.cycles.append(Cycle([WriteOperation(0x01, 'S', 'DL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([WriteOperation(0x01, 'S', 'P')]))
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'IR'), IncrementOperation('PCL', 'PCH')]))

    @property
    def name(self):
        return 'PLP'

    @property
    def opcode(self):
        return 0x28

    @property
    def description(self):
        return 'Pull Processor Status from Stack'
