from .branch import BranchInstruction


class Bcs(BranchInstruction):
    def meets_branch_condition(self, processor):
        return processor.p.c
