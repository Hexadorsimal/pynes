from .flag import Flag


class ZeroFlag(Flag):
    def update(self, value):
        if value == 0:
            self.set()
        else:
            self.clear()
