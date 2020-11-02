from nes.processors.registers import Register


class PpuAddr(Register):
    def __init__(self):
        self.addr = 0x0000

    @property
    def value(self):
        return self.addr

    @value.setter
    def value(self, lo):
        self.addr &= 0xFF
        self.addr <<= 8
        self.addr |= lo
