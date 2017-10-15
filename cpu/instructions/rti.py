from ..cycle import Cycle
from ..operation import ReadOperation, IncrementOperation
from ..implied_instruction import ImpliedInstruction


class Rti(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'IR')]))
        self.cycles.append(Cycle([ReadOperation(0x01, 'S', 'DL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(0x01, 'S', 'P'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(0x01, 'S', 'PCL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(0x01, 'S', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'IR'), IncrementOperation('PCL', 'PCH')]))

    @property
    def name(self):
        return 'RTI'

    @property
    def opcode(self):
        return 0x40

    @property
    def description(self):
        return 'Return from Interrupt'
