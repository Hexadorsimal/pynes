class Instruction:
    def __init__(self):
        self.cycles = []

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
