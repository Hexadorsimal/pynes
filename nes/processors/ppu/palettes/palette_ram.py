from nes.bus.devices.memory import Memory


class PaletteRam(Memory):
    def __init__(self):
        self.palette = bytearray(32)
        super().__init__(len(self.palette))

    def read(self, addr):
        addr = addr & 0x001F
        if addr & 0x03:
            return self.palette[addr]
        else:
            return self.palette[0]

    def write(self, addr, value):
        addr = addr & 0x001F
        self.palette[addr] = value
