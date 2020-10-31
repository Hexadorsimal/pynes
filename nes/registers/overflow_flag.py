from .flag import Flag


class OverflowFlag(Flag):
    def update(self, value):
        if value:
            self.set()
        else:
            self.clear()
