from nes.bus import BusDevice


class Cartridge:
    def __init__(self, rom_file):
        self.rom_file = rom_file

    @property
    def cpu_device(self):
        return BusDevice('cartridge cpu device')

    @property
    def ppu_device(self):
        return BusDevice('cartridge ppu device')

    @property
    def vram_mirroring_mode(self):
        return self.rom_file.header.vram_mirroring_mode

