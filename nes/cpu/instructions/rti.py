from ..cycle import Cycle
from ..operation import ReadOperation, IncrementOperation
from ..implied_instruction import ImpliedInstruction
from ...memory.address import AbsoluteAddress, StackAddress


class Rti(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'DL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'P'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'PCL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementOperation('PCL', 'PCH')]))

    @property
    def name(self):
        return 'RTI'

    @property
    def opcode(self):
        return 0x40

    @property
    def description(self):
        return 'Return from Interrupt'
