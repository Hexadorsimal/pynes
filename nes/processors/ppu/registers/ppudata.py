from nes.processors.registers import Register


class PpuData(Register):
    def __init__(self, ppu):
        self.ppu = ppu

    @property
    def value(self):
        # read from vram at the address in PPUADDR
        # increment PPUADDR by amount specified in PPUCTRL
        data = self.ppu.read(self.ppu.register_set.ppuaddr.value)
        self.ppu.register_set.ppuaddr.value += self.ppu.register_set.ppuctrl.vram_address_increment
        return data

    @value.setter
    def value(self, data):
        # write data to vram at the address in PPUADDR
        # increment PPUADDR by amount specified in PPUCTRL
        self.ppu.write(self.ppu.register_set.ppuaddr.value, data)
        self.ppu.register_set.ppuaddr.value += self.ppu.register_set.ppuctrl.vram_address_increment
