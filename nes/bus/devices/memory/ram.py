from .memory import Memory


class Ram(Memory):
    def __init__(self, size):
        super().__init__(size)
        self.data = bytearray(size)

    def read(self, addr):
        return self.data[addr]

    def write(self, addr, data):
        self.data[addr] = data
