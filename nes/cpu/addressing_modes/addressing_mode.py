class AddressingMode:
    def __init__(self):
        self.cycles = None

    @property
    def size(self):
        raise NotImplementedError
