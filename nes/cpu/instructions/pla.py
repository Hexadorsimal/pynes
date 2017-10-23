from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ReadMicroinstruction, WriteMicroinstruction, IncrementMicroinstruction
from nes.memory import AbsoluteAddress, StackAddress
from .implied_instruction import ImpliedInstruction


class Pla(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([WriteMicroinstruction(StackAddress('S'), 'DL'), IncrementMicroinstruction('S')]))
        self.cycles.append(Cycle([WriteMicroinstruction(StackAddress('S'), 'A')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementMicroinstruction('PCL')]))

    @property
    def name(self):
        return 'PLA'

    @property
    def opcode(self):
        return 0x68

    @property
    def description(self):
        return 'Pull Accumulator from Stack'
