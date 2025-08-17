from .branch import BranchInstruction
from ... import Cpu


class BranchIfClearInstruction(BranchInstruction):
    flag_name = None

    def meets_branch_condition(self, cpu: Cpu) -> bool:
        return not bool(cpu.p.flags[self.flag_name])
