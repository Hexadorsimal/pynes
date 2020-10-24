from nes.registers.register import Register


class PpuAddr(Register):
    def __init__(self, addr=0x0000):
        self.addr = addr

    def write(self, data):
        self.addr &= 0xFF
        self.addr <<= 8
        self.addr |= data
