from .memory_area import MemoryArea


class Ram(MemoryArea):
    def __init__(self, start, apparent_size, actual_size):
        super().__init__(start, apparent_size)
        self._actual_size = actual_size
        self._data = bytearray[actual_size]

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

    def read(self, addr):
        offset = addr - self.start
        non_mirrored_offset = offset % self._actual_size
        return self._data[non_mirrored_offset]

    def write(self, addr, data):
        offset = addr - self.start
        non_mirrored_offset = offset % self._actual_size
        self._data[non_mirrored_offset] = data
