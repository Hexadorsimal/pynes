from .branch import BranchInstruction


class BranchIfClearInstruction(BranchInstruction):
    flag_name = None

    def meets_branch_condition(self, processor):
        return not bool(processor.p.flags[self.flag_name])
