from .rom_file import RomFile
from .mmc_factory import MmcFactory


class Cartridge:
    def __init__(self, mmc):
        self.mmc = mmc

    @staticmethod
    def create(filename):
        rom_file = RomFile.load(filename)
        factory = MmcFactory()
        mmc = factory.create_mmc(rom_file)
        return Cartridge(mmc)
