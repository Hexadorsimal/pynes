from .pull import PullInstruction


class Pla(PullInstruction):
    dst_reg = 'a'
    update_flags = True
