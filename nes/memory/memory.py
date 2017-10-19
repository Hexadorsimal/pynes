class Memory:
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    def read(self, addr):
        raise NotImplementedError

    def write(self, addr, data):
        raise NotImplementedError
