from nes.memory import MemoryMap


class PpuRegisterSet(MemoryMap):
    def __init__(self, ppu):
        super().__init__(8)
        self.ppu = ppu

    def read(self, logical_addr):
        if logical_addr == 0:
            return self.ppu.ppu_controller
        elif logical_addr == 1:
            return self.ppu.ppu_mask
        elif logical_addr == 2:
            return self.ppu.ppu_status
        elif logical_addr == 3:
            return self.ppu.oam_address
        elif logical_addr == 4:
            return self.ppu.oam_data
        elif logical_addr == 5:
            return self.ppu.ppu_scroll
        elif logical_addr == 6:
            return self.ppu.ppu_address
        elif logical_addr == 7:
            return  self.ppu.ppu_data

    def write(self, logical_addr, value):
        if logical_addr == 0:
            self.ppu.ppu_controller = value
        elif logical_addr == 1:
            self.ppu.ppu_mask = value
        elif logical_addr == 2:
            self.ppu.ppu_status = value
        elif logical_addr == 3:
            self.ppu.oam_address = value
        elif logical_addr == 4:
            self.ppu.oam_data = value
        elif logical_addr == 5:
            self.ppu.ppu_scroll = value
        elif logical_addr == 6:
            self.ppu.ppu_address = value
        elif logical_addr == 7:
            self.ppu.ppu_data = value
