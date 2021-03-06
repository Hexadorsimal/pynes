from .memory import Memory


class Rom(Memory):
    def __init__(self, size, data):
        super().__init__(size)
        self.data = data

    def read(self, addr):
        return self.data[addr]

    def write(self, addr, value):
        raise RuntimeError('You cannot write to ROM')
