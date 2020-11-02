from nes.processors.registers import Register


class OamAddr(Register):
    def __init__(self):
        self.addr = 0x00

    @property
    def value(self):
        return self.addr

    @value.setter
    def value(self, addr):
        self.addr = addr
