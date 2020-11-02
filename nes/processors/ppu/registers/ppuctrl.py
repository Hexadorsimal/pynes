from nes.processors.registers import Register


class PpuCtrl(Register):
    nametable_addresses = [
        0x2000,
        0x2400,
        0x2800,
        0x2C00,
    ]

    def __init__(self, data=0):
        self.data = data

    @property
    def value(self):
        return self.data

    @value.setter
    def value(self, value):
        self.data = value
        
    @property
    def base_nametable_address(self):
        index = self.data & 0x03
        return self.nametable_addresses[index]

    @property
    def vram_address_increment(self):
        if self.data & 0x04:
            return 32
        else:
            return 1

    @property
    def sprite_pattern_table_address(self):
        if self.data & 0x08:
            return 0x1000
        else:
            return 0x0000

    @property
    def background_pattern_table_address(self):
        if self.data & 0x10:
            return 0x1000
        else:
            return 0x0000

    @property
    def sprite_size(self):
        if self.data & 0x20:
            return 8, 16
        else:
            return 8, 8

    @property
    def master_slave_select(self):
        if self.data & 0x40:
            return 'master'
        else:
            return 'slave'

    @property
    def generate_nmi_on_vblank(self):
        if self.data & 0x80:
            return True
        else:
            return False
