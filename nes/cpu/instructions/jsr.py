from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import DecrementMicroinstruction, IncrementMicroinstruction, ReadMicroinstruction, WriteMicroinstruction
from .absolute_instruction import AbsoluteInstruction


class Jsr(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction('PCH', 'PCL', 'ADL'), IncrementMicroinstruction('PCL', 'PCH')]))
        self.cycles.append(Cycle([]))
        self.cycles.append(Cycle([WriteMicroinstruction(0x01, 'S', 'PCH'), DecrementMicroinstruction('S')]))
        self.cycles.append(Cycle([WriteMicroinstruction(0x01, 'S', 'PCL'), DecrementMicroinstruction('S')]))
        self.cycles.append(Cycle([ReadMicroinstruction('PCH', 'PCL', 'ADH'), IncrementMicroinstruction('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadMicroinstruction('ADH', 'ADL', 'IR')]))

    @property
    def name(self):
        return 'JSR'

    @property
    def opcode(self):
        return 0x20

    @property
    def description(self):
        return 'Jump to Subroutine'
