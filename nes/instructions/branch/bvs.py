from .branch import BranchInstruction


class Bvs(BranchInstruction):
    def meets_branch_condition(self, processor):
        return processor.p.v
