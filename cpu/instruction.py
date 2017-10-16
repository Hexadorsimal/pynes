from .cycle import Cycle
from .operation import ReadOperation, IncrementOperation


class Instruction:
    def __init__(self):
        self.cycles = [Cycle([ReadOperation('PCH', 'PCL', 'IR'), IncrementOperation('PCL', 'PCH')])]

    @property
    def name(self):
        raise NotImplementedError

    @property
    def opcode(self):
        raise NotImplementedError

    @property
    def size(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError
