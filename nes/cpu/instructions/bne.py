from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BranchMicroinstruction
from .relative_instruction import RelativeInstruction


class Bne(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchMicroinstruction('Z', False)]))

    @property
    def name(self):
        return 'BNE'

    @property
    def opcode(self):
        return 0xD0

    @property
    def description(self):
        return 'Branch on Result not Zero'
