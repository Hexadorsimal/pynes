class Instruction:
    def __init__(self):
        self.cycles = []
        self.addressing_modes = {}

    def __repr__(self):
        return self.name

    @property
    def name(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError
