class AddressingMode:
    def __init__(self):
        self.cycles = []

    @property
    def size(self):
        raise NotImplementedError
