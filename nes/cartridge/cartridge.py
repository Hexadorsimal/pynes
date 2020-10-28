from nes.bus import Bus


class Cartridge:
    def __init__(self, rom_file):
        self.rom_file = rom_file
        self.buses = {
            'cpu': Bus('cartridge cpu bus'),
            'ppu': Bus('cartridge ppu bus'),
        }

    @property
    def name(self):
        return 'cartridge'

    @property
    def vram_mirroring_mode(self):
        return self.rom_file.header.vram_mirroring_mode
