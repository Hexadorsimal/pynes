from .memory import Memory


class Ram(Memory):
    def __init__(self, size):
        super().__init__(size)
        self._data = bytearray[size]

    def read(self, addr):
        return self._data[addr]

    def write(self, addr, data):
        self._data[addr] = data
