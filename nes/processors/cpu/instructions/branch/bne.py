from .branch import BranchInstruction


class Bne(BranchInstruction):
    def meets_branch_condition(self, processor):
        return not processor.p.z
