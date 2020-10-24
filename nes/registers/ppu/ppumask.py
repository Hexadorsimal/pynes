from nes.registers.register import Register


class PpuMask(Register):
    """
    7  bit  0
    ---- ----
    BGRs bMmG
    |||| ||||
    |||| |||+- Greyscale (0: normal color, 1: produce a greyscale display)
    |||| ||+-- 1: Show background in leftmost 8 pixels of screen, 0: Hide
    |||| |+--- 1: Show sprites in leftmost 8 pixels of screen, 0: Hide
    |||| +---- 1: Show background
    |||+------ 1: Show sprites
    ||+------- Emphasize red
    |+-------- Emphasize green
    +--------- Emphasize blue
    """
    def __init__(self, data=0):
        self.data = data

    def write(self, data):
        self.data = data

    @property
    def grayscale(self):
        return self.data & 0x01

    @property
    def show_background_in_leftmost_8_pixels(self):
        return self.data & 0x02
    
    @property
    def show_sprites_in_leftmost_8_pixels(self):
        return self.data & 0x04
    
    @property
    def show_background(self):
        return self.data & 0x08
    
    @property
    def show_sprites(self):
        return self.data & 0x10
    
    @property
    def emphasize_red(self):
        return self.data & 0x20

    @property
    def emphasize_green(self):
        return self.data & 0x40

    @property
    def emphasize_blue(self):
        return self.data &  0x80
