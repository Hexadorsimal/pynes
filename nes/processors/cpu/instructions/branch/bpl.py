from .branch_if_clear import BranchIfClearInstruction


class Bpl(BranchIfClearInstruction):
    flag_name = 'n'
