from nes.cpu.cycle import Cycle
from nes.cpu.operations import BranchOperation
from .relative_instruction import RelativeInstruction


class Bcs(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchOperation('C', True)]))

    @property
    def name(self):
        return 'BCS'

    @property
    def opcode(self):
        return 0xB0

    @property
    def description(self):
        return 'Branch on Carry Set'
