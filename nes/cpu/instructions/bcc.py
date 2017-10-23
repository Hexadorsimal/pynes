from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BranchMicroinstruction
from .relative_instruction import RelativeInstruction


class Bcc(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchMicroinstruction('C', False)]))

    @property
    def name(self):
        return 'BCC'

    @property
    def opcode(self):
        return 0x90

    @property
    def description(self):
        return 'Branch on Carry Clear'
