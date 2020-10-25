from .flag import Flag


class ZFlag(Flag):
    def update(self, value):
        if value == 0:
            self.set()
        else:
            self.clear()
