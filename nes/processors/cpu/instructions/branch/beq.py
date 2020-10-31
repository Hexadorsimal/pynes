from .branch import BranchInstruction


class Beq(BranchInstruction):
    def meets_branch_condition(self, processor):
        return bool(processor.p.z)
