from .flag import Flag


class NegativeFlag(Flag):
    def update(self, value):
        if value & 0x80 != 0:
            self.set()
        else:
            self.clear()
