from .mmc import Nrom


class MmcFactory:
    def __init__(self):
        self.mmc_map = {
            0: Nrom
        }

    def create_mmc(self, rom_file):
        mapper = rom_file.header.mapper
        if mapper in self.mmc_map.keys():
            return self.mmc_map[mapper](rom_file)
