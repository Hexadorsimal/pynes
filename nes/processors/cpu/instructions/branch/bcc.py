from .branch_if_clear import BranchIfClearInstruction


class Bcc(BranchIfClearInstruction):
    flag_name = 'c'
