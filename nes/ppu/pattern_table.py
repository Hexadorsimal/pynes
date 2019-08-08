from .pattern_tile import PatternTile


class PatternTable:
    def __init__(self, data=None):
        self.data = data
        if not self.data:
            self.data = bytearray(256)

    def get_tile(self, x, y):
        addr = y * 16 + x
        return PatternTile(self.data[addr], self.data[addr+1])
