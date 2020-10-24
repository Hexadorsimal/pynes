class Cartridge:
    def __init__(self, rom_file):
        self.rom_file = rom_file

    def connect(self, buses):
        raise NotImplementedError

    def disconnect(self, buses):
        raise NotImplementedError

    @property
    def vram_mirroring_mode(self):
        return self.rom_file.header.vram_mirroring_mode
