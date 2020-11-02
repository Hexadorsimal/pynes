from nes.bus import BusDevice
from .registers import PpuAddr, PpuCtrl, PpuData, PpuMask, PpuScroll, PpuStatus, OamAddr, OamData


class PpuRegisterSet(BusDevice):
    def __init__(self, ppu):
        self.registers = [
            PpuCtrl(),
            PpuMask(),
            PpuStatus(),
            OamAddr(),
            OamData(ppu),
            PpuScroll(ppu),
            PpuAddr(),
            PpuData(ppu),
        ]

    def read(self, addr):
        logical_addr = addr % len(self.registers)
        return self.registers[logical_addr].value

    def write(self, addr, value):
        logical_addr = addr % len(self.registers)
        self.registers[logical_addr].value = value

    @property
    def ppuctrl(self):
        return self.registers[0]

    @property
    def ppumask(self):
        return self.registers[1]

    @property
    def ppustatus(self):
        return self.registers[2]

    @property
    def oamaddr(self):
        return self.registers[3]

    @property
    def oamdata(self):
        return self.registers[4]

    @property
    def ppuscroll(self):
        return self.registers[5]

    @property
    def ppuaddr(self):
        return self.registers[6]

    @property
    def ppudata(self):
        return self.registers[7]
