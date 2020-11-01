from .branch_if_set import BranchIfSetInstruction


class Bmi(BranchIfSetInstruction):
    flag_name = 'n'
