from ...memory import PrgRam, AddressRange
from .mmc import Mmc


class Nrom(Mmc):
    def __init__(self, rom_file):
        super().__init__(0xA000, rom_file)
        self.prg_ram = PrgRam(0x2000)

        self.add_memory(AddressRange(0x0000, 0x2000), self.prg_ram)
        self.add_memory(AddressRange(0x2000, 0x8000), self.prg_rom_pages[0])
