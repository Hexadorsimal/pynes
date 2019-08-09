from nes.bus import BusDevice
from nes.cartridge.ines import VramMirroringMode


class NameTableRam(BusDevice):
    def __init__(self):
        self.data = bytearray(0x0800)

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

    def handle_read_request(self, request):
        if 0x2000 <= request.addr <= 0x2FFF:
            addr = self.translate_address(request.addr, request.vram_mirroring_mode)
            if addr:
                return self.data[addr]

    def handle_write_request(self, request):
        if 0x2000 <= request.addr <= 0x2FFF:
            addr = self.translate_address(request.addr, request.vram_mirroring_mode)
            if addr:
                self.data[addr] = request.data
