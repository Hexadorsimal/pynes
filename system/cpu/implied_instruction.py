from .instruction import Instruction


class ImpliedInstruction(Instruction):
    def __init__(self):
        super().__init__()

    @property
    def size(self):
        return 1
