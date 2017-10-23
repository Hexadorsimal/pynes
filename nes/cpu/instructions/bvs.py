from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BranchMicroinstruction
from .relative_instruction import RelativeInstruction


class Bvs(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchMicroinstruction('V', True)]))

    @property
    def name(self):
        return 'BVS'

    @property
    def opcode(self):
        return 0x70

    @property
    def description(self):
        return 'Branch on Overflow Set'
