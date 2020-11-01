from .branch_if_set import BranchIfSetInstruction


class Beq(BranchIfSetInstruction):
    flag_name = 'z'
