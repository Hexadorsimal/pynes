from .branch_if_clear import BranchIfClearInstruction


class Bne(BranchIfClearInstruction):
    flag_name = 'n'
