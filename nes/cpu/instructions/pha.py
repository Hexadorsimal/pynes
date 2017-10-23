from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ReadMicroinstruction, WriteMicroinstruction, IncrementMicroinstruction, DecrementMicroinstruction
from nes.memory import AbsoluteAddress, StackAddress
from .implied_instruction import ImpliedInstruction


class Pha(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([WriteMicroinstruction(StackAddress('S'), 'A'), DecrementMicroinstruction('S')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementMicroinstruction('PCL')]))

    @property
    def name(self):
        return 'PHA'

    @property
    def opcode(self):
        return 0x48

    @property
    def description(self):
        return 'Push Accumulator on Stack'
