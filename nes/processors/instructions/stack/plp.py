from .pull import PullInstruction


class Plp(PullInstruction):
    dst_reg = 'p'
    update_flags = False
