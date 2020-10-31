from .branch import BranchInstruction


class Bcc(BranchInstruction):
    def meets_branch_condition(self, processor):
        return not processor.p.c
