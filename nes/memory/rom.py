from .memory import Memory


class Rom(Memory):
    def __init__(self, size):
        super().__init__(size)
        self._data = bytearray(size)

    def read(self, addr):
        return self._data[addr]

    def write(self, addr, data):
        raise RuntimeError('You cannot write to ROM')
