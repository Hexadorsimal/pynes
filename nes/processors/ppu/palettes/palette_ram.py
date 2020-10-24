from nes.bus import BusDevice


class PaletteRam(BusDevice):
    def __init__(self):
        super().__init__('palette ram')
        self.palette = bytearray(32)

    def read(self, addr):
        if 0x3F00 <= addr <= 0x3FFF:
            addr = addr & 0x001F
            if addr & 0x03:
                return self.palette[addr]
            else:
                return self.palette[0]

    def write(self, addr, value):
        if 0x3F00 <= addr <= 0x3FFF:
            addr = addr & 0x001F
            self.palette[addr] = value
