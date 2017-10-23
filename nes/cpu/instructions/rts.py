from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ReadMicroinstruction, IncrementMicroinstruction
from nes.memory import AbsoluteAddress, StackAddress
from .implied_instruction import ImpliedInstruction


class Rts(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'DL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(StackAddress('S'), 'DL'), IncrementMicroinstruction('S')]))
        self.cycles.append(Cycle([ReadMicroinstruction(StackAddress('S'), 'PCL'), IncrementMicroinstruction('S')]))
        self.cycles.append(Cycle([ReadMicroinstruction(StackAddress('S'), 'PCH')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'DL'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementMicroinstruction('PCL')]))

    @property
    def name(self):
        return 'RTS'

    @property
    def opcode(self):
        return 0x60

    @property
    def description(self):
        return 'Return from Subroutine'
