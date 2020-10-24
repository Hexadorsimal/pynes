from nes.bus import BusDevice


class PpuRegisterSet(BusDevice):
    def __init__(self, ppu):
        super().__init__(8)
        self.ppu = ppu
        self.registers = [
            ppu.ppu_controller,
            ppu.ppu_mask,
            ppu.ppu_status,
            ppu.oam_address,
            ppu.oam_data,
            ppu.ppu_scroll,
            ppu.address,
            ppu.ppu_data,
        ]

    def read(self, logical_addr):
        return self.registers[logical_addr].read()

    def write(self, logical_addr, value):
        self.registers[logical_addr].write(value)
