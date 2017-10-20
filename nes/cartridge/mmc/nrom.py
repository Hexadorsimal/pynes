from ...memory import Ram
from .mmc import Mmc


class Nrom(Mmc):
    def __init__(self, rom_file):
        super().__init__(0x10000)
        self.prh_ram = Ram(0x2000)
        self.prg_rom = rom_file.prg_rom_pages
        self.chr_rom = rom_file.chr_rom_pages
