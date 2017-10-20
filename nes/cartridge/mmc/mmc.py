from ...memory import MemoryMap, PrgRom, ChrRom


class Mmc(MemoryMap):
    def __init__(self, size, rom_file):
        super().__init__(size)
        self.prg_rom_pages = []
        self.chr_rom_pages = []

        for prg_rom_page in rom_file.prg_rom_pages:
            self.prg_rom_pages.append(PrgRom(prg_rom_page))

        for chr_rom_page in rom_file.chr_rom_pages:
            self.chr_rom_pages.append(ChrRom(chr_rom_page))
