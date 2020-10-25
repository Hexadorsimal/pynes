from .flag import Flag


class NFlag(Flag):
    def update(self, value):
        if value & 0x80:
            self.set()
        else:
            self.clear()
