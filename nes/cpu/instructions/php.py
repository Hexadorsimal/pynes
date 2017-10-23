from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ReadMicroinstruction, WriteMicroinstruction, IncrementMicroinstruction, DecrementMicroinstruction
from nes.memory import AbsoluteAddress, StackAddress
from .implied_instruction import ImpliedInstruction


class Php(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([WriteMicroinstruction(StackAddress('S'), 'P'), DecrementMicroinstruction('S')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementMicroinstruction('PCL')]))

    @property
    def name(self):
        return 'PHP'

    @property
    def opcode(self):
        return 0x08

    @property
    def description(self):
        return 'Push Processor Status on Stack'
