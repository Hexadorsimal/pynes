from nes.bus import BusDevice
from nes.bus.devices.cartridge.ines import VramMirroringMode


class NameTableRam(BusDevice):
    def __init__(self, vram_mirroring_mode=VramMirroringMode.single_screen):
        super().__init__('name table ram')
        self.data = bytearray(0x0800)
        self.vram_mirroring_mode = vram_mirroring_mode

    @staticmethod
    def translate_address(logical_addr, vram_mirroring_mode):
        addr = logical_addr & 0x0FFF

        if vram_mirroring_mode == VramMirroringMode.horizontal:
            addr = addr & ~0x0400
            if addr >= 0x0800:
                addr -= 0x0400
        elif vram_mirroring_mode == VramMirroringMode.vertical:
            addr = addr & ~0x0800
        elif vram_mirroring_mode == VramMirroringMode.single_screen:
            addr = addr & ~0x0C00
        elif vram_mirroring_mode == VramMirroringMode.four_screen:
            if addr >= 0x0800:
                return None  # let another ram chip on the bus handle this

        return addr

    def read(self, addr):
        if 0x2000 <= addr <= 0x2FFF:
            addr = self.translate_address(addr, self.vram_mirroring_mode)
            if addr:
                return self.data[addr]

    def write(self, addr, value):
        if 0x2000 <= addr <= 0x2FFF:
            addr = self.translate_address(addr, self.vram_mirroring_mode)
            if addr:
                self.data[addr] = value
