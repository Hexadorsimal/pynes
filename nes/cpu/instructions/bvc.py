from nes.cpu.cycle import Cycle
from nes.cpu.operations import BranchOperation
from .relative_instruction import RelativeInstruction


class Bvc(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchOperation('V', False)]))

    @property
    def name(self):
        return 'BVC'

    @property
    def opcode(self):
        return 0x50

    @property
    def description(self):
        return 'Branch on Overflow Clear'
