from .branch import BranchInstruction


class BranchIfSetInstruction(BranchInstruction):
    flag_name = None

    def meets_branch_condition(self, processor):
        return bool(processor.p.flags[self.flag_name])
