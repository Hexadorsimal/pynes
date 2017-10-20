from ...memory import Ram, AddressRange
from .mmc import Mmc


class Nrom(Mmc):
    def __init__(self, rom_file):
        super().__init__(0xA000)
        self.prg_ram = Ram(0x2000)
        # TODO: These need to go inside a Rom object
        self.prg_rom = rom_file.prg_rom_pages
        self.chr_rom = rom_file.chr_rom_pages

        self.add_memory(AddressRange(0x0000, 0x2000), self.prg_ram)
        self.add_memory(AddressRange(0x2000, 0x8000), self.prg_rom)
