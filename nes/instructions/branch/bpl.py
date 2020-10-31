from .branch import BranchInstruction


class Bpl(BranchInstruction):
    def meets_branch_condition(self, processor):
        return not processor.p.n
