from enum import Enum, IntFlag


class Flags6(IntFlag):
    vertical_mirroring = 0x01
    contains_sram = 0x02
    contains_trainer = 0x04
    four_screen_vram = 0x08
    mapper_lower = 0xf0


class VramMirroringMode(Enum):
    horizontal = 0
    vertical = 1
    single_screen = 2
    four_screen = 3


class Flags7(IntFlag):
    versus = 0x01
    playchoice10 = 0x02
    contains_nes2 = 0x0c
    mapper_upper = 0xf0


class Flags9(IntFlag):
    tv_system = 0x01
    reserved = 0xfe


class iNesHeader:
    prg_rom_page_size = 16 * 1024
    chr_rom_page_size = 8 * 1024
    prg_ram_page_size = 8 * 1024

    def __init__(self, header):
        self.header = header

    @property
    def vram_mirroring_mode(self):
        h6 = self.header[6]

        if h6 & Flags6.four_screen_vram:
            if h6 & Flags6.vertical_mirroring:
                return VramMirroringMode.four_screen
            else:
                return VramMirroringMode.single_screen
        else:
            if h6 & Flags6.vertical_mirroring:
                return VramMirroringMode.vertical
            else:
                return VramMirroringMode.horizontal

    @property
    def prg_rom_page_count(self):
        return self.header[4]

    @property
    def prg_rom_size(self):
        return self.prg_rom_page_count * self.prg_rom_page_size

    @property
    def chr_rom_page_count(self):
        return self.header[5]

    @property
    def chr_rom_size(self):
        return self.chr_rom_page_count * self.chr_rom_page_size

    @property
    def prg_ram_page_count(self):
        return self.header[8]

    @property
    def prg_ram_size(self):
        return self.prg_ram_page_count * self.prg_ram_page_size

    @property
    def mapper(self):
        upper = self.header[7] & Flags7.mapper_upper.value
        lower = (self.header[6] & Flags6.mapper_lower.value)
        return upper | (lower >> 4)

    @property
    def contains_sram(self):
        if self.header[6] & Flags6.contains_sram.value:
            return True
        else:
            return False

    @property
    def four_screen_mode(self):
        if self.header[6] & Flags6.four_screen_vram.value:
            return True
        else:
            return False

    @property
    def contains_trainer(self):
        if self.header[6] & Flags6.contains_trainer.value:
            return True
        else:
            return False

    @property
    def is_playchoice10(self):
        if self.header[7] & Flags7.playchoice10.value:
            return True
        else:
            return False

    @property
    def is_versus(self):
        if self.header[7] & Flags7.versus.value:
            return True
        else:
            return False
