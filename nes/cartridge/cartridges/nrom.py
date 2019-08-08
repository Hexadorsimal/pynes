from nes.memory import PrgRom, ChrRom
from nes.bus import ReadResponse
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

    def handle_cpu_read_request(self, request):
        if 0x8000 <= request.addr <= 0xBFFF:
            return ReadResponse(request, self, self.prg_rom_pages[0].read(request.addr - 0x8000))
        elif 0xC000 <= request.addr <= 0xCFFF:
            page = 1 if len(self.prg_rom_pages) > 1 else 0
            return ReadResponse(request, self, self.prg_rom_pages[page].read(request.addr - 0xC000))

    def handle_ppu_read_request(self, request):
        if 0x0000 <= request.addr <= 0x1FFF:
            return ReadResponse(request, self, self.chr_rom_pages[0].read(request.addr))
