from nes.memory import PrgRom, ChrRom
from ..cartridge import Cartridge


class NromCartridge(Cartridge):
    def __init__(self, rom_file):
        super().__init__(rom_file)
        self.prg_rom_pages = []
        self.chr_rom_pages = []

        for prg_rom_page in rom_file.prg_rom_pages:
            self.prg_rom_pages.append(PrgRom(prg_rom_page))

        for chr_rom_page in rom_file.chr_rom_pages:
            self.chr_rom_pages.append(ChrRom(chr_rom_page))

    def cpu_read(self, addr):
        if 0x8000 <= addr <= 0xBFFF:
            return self.prg_rom_pages[0].read(addr - 0x8000)
        elif 0xC000 <= addr <= 0xCFFF:
            page = 1 if len(self.prg_rom_pages) > 1 else 0
            return self.prg_rom_pages[page].read(addr - 0xC000)

    def ppu_read(self, addr):
        if 0x0000 <= addr <= 0x1FFF:
            return self.chr_rom_pages[0].read(addr)
