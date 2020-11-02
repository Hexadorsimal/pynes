from nes.bus import BusDevice


class PpuRegisterSet(BusDevice):
    def __init__(self, ppu):
        self.registers = [
            ppu.ppuctrl,
            ppu.ppumask,
            ppu.ppustatus,
            ppu.oamaddr,
            ppu.oamdata,
            ppu.ppuscroll,
            ppu.ppuaddr,
            ppu.ppudata,
        ]

    def read(self, addr):
        logical_addr = addr % len(self.registers)
        return self.registers[logical_addr].value

    def write(self, addr, value):
        logical_addr = addr % len(self.registers)
        self.registers[logical_addr].value = value
