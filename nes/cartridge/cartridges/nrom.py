from nes.memory import PrgRom, ChrRom
from ..cartridge import Cartridge


class NromCartridge(Cartridge):
    def __init__(self, rom_file):
        super().__init__(rom_file)
        self.prg_rom_pages = []
        self.chr_rom_pages = []

        for index, prg_rom_page in enumerate(rom_file.prg_rom_pages):
            self.prg_rom_pages.append(PrgRom(f'PRG{index}', prg_rom_page))

        for index, chr_rom_page in enumerate(rom_file.chr_rom_pages):
            self.chr_rom_pages.append(ChrRom(f'CHR{index}', chr_rom_page))

        if len(self.prg_rom_pages) == 1:
            self.buses['cpu'].attach_device(self.prg_rom_pages[0], addr=0x8000, size=0x8000)
        else:
            self.buses['cpu'].attach_device(self.prg_rom_pages[0], addr=0x8000, size=0x4000)
            self.buses['cpu'].attach_device(self.prg_rom_pages[1], addr=0xC000, size=0x4000)

        if self.chr_rom_pages:
            self.buses['ppu'].attach_device(self.chr_rom_pages[0], addr=0x0000, size=0x2000)
