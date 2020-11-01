from .branch_if_set import BranchIfSetInstruction


class Bcs(BranchIfSetInstruction):
    flag_name = 'c'
