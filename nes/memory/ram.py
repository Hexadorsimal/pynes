from .memory import Memory


class Ram(Memory):
    def __init__(self, size):
        self.data = bytearray(size)
        super().__init__(len(self.data))

    @property
    def name(self):
        return 'ram'

    def read(self, addr):
        return self.data[addr]

    def write(self, addr, data):
        self.data[addr] = data
