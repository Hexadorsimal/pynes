class Instruction:
    def __init__(self):
        self.cycles = []

    def __repr__(self):
        return '{opcode}: {name}'.format(opcode=hex(self.opcode), name=self.name)

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
