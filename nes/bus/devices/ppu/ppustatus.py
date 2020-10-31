from nes.processors.cpu.registers import Register


class PpuStatus(Register):
    def __init__(self):
        self.sprite_overflow = 0
        self.sprite0_hit = 0
        self.in_vblank = 0

    def read(self):
        data = 0
        data |= self.in_vblank << 7
        data |= self.sprite0_hit << 6
        data |= self.sprite_overflow << 5
        return data
