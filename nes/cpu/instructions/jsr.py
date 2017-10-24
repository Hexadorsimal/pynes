from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import DecrementMicroinstruction, IncrementMicroinstruction, ReadMicroinstruction, WriteMicroinstruction
from nes.memory import AbsoluteAddress, StackAddress
from .absolute_instruction import AbsoluteInstruction


class Jsr(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'ADL'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([]))
        self.cycles.append(Cycle([WriteMicroinstruction(StackAddress('S'), 'PCH'), DecrementMicroinstruction('S')]))
        self.cycles.append(Cycle([WriteMicroinstruction(StackAddress('S'), 'PCL'), DecrementMicroinstruction('S')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'ADH'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('ADH', 'ADL'), 'IR')]))

    @property
    def name(self):
        return 'JSR'

    @property
    def opcode(self):
        return 0x20

    @property
    def description(self):
        return 'Jump to Subroutine'
