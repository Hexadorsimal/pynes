class AddressRange:
    def __init__(self, start: int, size: int):
        self.start = start
        self.size = size

    def __repr__(self):
        return f'{self.start:#x} - {self.end:#x}'

    def __contains__(self, addr: int):
        return self.start <= addr <= self.end

    @property
    def end(self):
        return self.start + self.size - 1
