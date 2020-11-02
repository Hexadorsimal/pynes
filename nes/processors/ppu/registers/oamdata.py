from nes.processors.registers import Register


class OamData(Register):
    def __init__(self, ppu):
        self.ppu = ppu

    @property
    def value(self):
        addr = self.ppu.oamaddr.addr
        return self.ppu.oam.read(addr)

    @value.setter
    def value(self, data):
        addr = self.ppu.oamaddr.addr
        self.ppu.oam.write(addr, data)
        self.ppu.oamaddr.value += 1
