from .register import Register


class FlagRegister(Register):
    def __init__(self, flags):
        self.flags = flags

    def __getattr__(self, item):
        if item in self.flags:
            return self.flags[item]

    @property
    def value(self):
        bits = 0
        for flag in self.flags.values():
            if flag:
                bits |= flag.mask

        return bits

    @value.setter
    def value(self, bits):
        for flag in self.flags.values():
            if flag.mask & bits != 0:
                flag.set()
            else:
                flag.clear()
