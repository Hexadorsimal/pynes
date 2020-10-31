from .branch import BranchInstruction


class Bmi(BranchInstruction):
    def meets_branch_condition(self, processor):
        return processor.p.n
