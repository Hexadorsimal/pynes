from .flag import Flag


class CarryFlag(Flag):
    def update(self, value):
        if value:
            self.set()
        else:
            self.clear()
