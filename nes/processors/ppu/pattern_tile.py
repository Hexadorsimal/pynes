class PatternTile:
    def __init__(self, plane0, plane1):
        self.plane0 = plane0
        self.plane1 = plane1

    def get_bits(self, x, y):
        bit0 = (self.plane0 >> (7-x)) & 0x01
        bit1 = (self.plane1 >> (7-x)) & 0x01

        return (bit1 << 1) | bit0
