from nes.processors.registers import Register


class PpuScroll(Register):
    def __init__(self, ppu):
        self.ppu = ppu
        self.write_to_h = True

    @property
    def value(self):
        return None

    @value.setter
    def value(self, data):
        if self.write_to_h:
            self.ppu.registers['fh'].value = data
        else:
            self.ppu.registers['fv'].value = data

        self.write_to_h = not self.write_to_h
