from nes.cpu.cycle import Cycle
from nes.cpu.operations import ReadOperation, WriteOperation, IncrementOperation, DecrementOperation
from nes.memory import AbsoluteAddress, StackAddress
from .implied_instruction import ImpliedInstruction


class Pha(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([WriteOperation(StackAddress('S'), 'A'), DecrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementOperation('PCL')]))

    @property
    def name(self):
        return 'PHA'

    @property
    def opcode(self):
        return 0x48

    @property
    def description(self):
        return 'Push Accumulator on Stack'
