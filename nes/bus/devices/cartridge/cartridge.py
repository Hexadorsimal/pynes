from nes.bus import Bus


class Cartridge:
    CART_CPU_START = 0x6000
    PRG0_START = 0x8000 - CART_CPU_START
    PRG1_START = 0xC000 - CART_CPU_START
    PRG_SIZE = 0x4000

    CART_PPU_START = 0x0000
    CHR0_START = CART_PPU_START
    CHR_SIZE = 0x2000

    def __init__(self, rom_file):
        self.rom_file = rom_file
        self.buses = {
            'cpu': Bus('cartridge cpu bus'),
            'ppu': Bus('cartridge ppu bus'),
        }

    @property
    def name(self):
        raise NotImplementedError

    @property
    def vram_mirroring_mode(self):
        return self.rom_file.header.vram_mirroring_mode
