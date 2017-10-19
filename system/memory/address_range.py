class AddressRange:
    def __init__(self, start, size):
        self._start = start
        self._size = size

    def __contains__(self, addr):
        return self.start <= addr < self.end

    @property
    def size(self):
        return self._size

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self.start + self.size
