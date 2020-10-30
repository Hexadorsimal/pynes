from .flag import Flag


class OverflowFlag(Flag):
    def update(self, value):
        if value & 0x40:
            self.set()
        else:
            self.clear()
