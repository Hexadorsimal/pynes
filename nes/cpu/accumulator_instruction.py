from .instruction import Instruction


class AccumulatorInstruction(Instruction):
    def __init__(self):
        super().__init__()

    @property
    def size(self):
        return 1
