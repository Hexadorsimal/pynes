from nes.cpu.cycle import Cycle
from nes.cpu.operations import ReadOperation, IncrementOperation
from nes.memory import AbsoluteAddress, StackAddress
from .implied_instruction import ImpliedInstruction


class Rts(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'DL')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'DL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'PCL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'DL'), IncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementOperation('PCL')]))

    @property
    def name(self):
        return 'RTS'

    @property
    def opcode(self):
        return 0x60

    @property
    def description(self):
        return 'Return from Subroutine'
