from .cartridges import NromCartridge
from .rom_file import RomFile


class CartridgeFactory:
    cartridge_map = {
        0: NromCartridge,
    }

    @classmethod
    def create(cls, filename):
        rom_file = RomFile.load(filename)

        return cls.cartridge_map[rom_file.header.mapper](rom_file)
