from .branch import BranchInstruction
from ... import Cpu


class BranchIfSetInstruction(BranchInstruction):
    flag_name = None

    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return bool(cpu.p.flags[self.flag_name])
