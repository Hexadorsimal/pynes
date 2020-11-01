from .branch_if_clear import BranchIfClearInstruction


class Bvc(BranchIfClearInstruction):
    flag_name = 'v'
