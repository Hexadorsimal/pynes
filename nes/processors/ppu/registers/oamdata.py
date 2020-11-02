from nes.processors.registers import Register


class OamData(Register):
    def __init__(self, ppu):
        self.ppu = ppu

    def read(self):
        addr = self.ppu.oamaddr.addr
        return self.ppu.oam.read(addr)

    def write(self, data):
        addr = self.ppu.oamaddr.addr
        self.ppu.oam.write(addr, data)
