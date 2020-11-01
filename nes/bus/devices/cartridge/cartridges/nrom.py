from nes.bus.devices.memory import PrgRom, ChrRom
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

        if len(self.prg_rom_pages) == 1:
            self.buses['cpu'].attach_device('PRG0', self.prg_rom_pages[0], addr=self.PRG0_START, size=self.PRG_SIZE)
            self.buses['cpu'].attach_device('PRG0 Mirror', self.prg_rom_pages[0], addr=self.PRG1_START, size=self.PRG_SIZE)
        else:
            self.buses['cpu'].attach_device('PRG0', self.prg_rom_pages[0], addr=self.PRG0_START, size=self.PRG_SIZE)
            self.buses['cpu'].attach_device('PRG1', self.prg_rom_pages[1], addr=self.PRG1_START, size=self.PRG_SIZE)

        if self.chr_rom_pages:
            self.buses['ppu'].attach_device('CHR0', self.chr_rom_pages[0], addr=self.CHR0_START, size=self.CHR_SIZE)

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return 'NROM Cartridge'
