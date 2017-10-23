from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BranchMicroinstruction
from .relative_instruction import RelativeInstruction


class Beq(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchMicroinstruction('Z', True)]))

    @property
    def name(self):
        return 'BEQ'

    @property
    def opcode(self):
        return 0xF0

    @property
    def description(self):
        return 'Branch on Result Zero'
