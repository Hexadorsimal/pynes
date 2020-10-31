from .branch import BranchInstruction


class Bvc(BranchInstruction):
    def meets_branch_condition(self, processor):
        return not processor.p.v
