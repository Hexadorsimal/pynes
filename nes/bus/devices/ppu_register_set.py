from nes.bus import BusDevice
from .ppu import PpuAddr, PpuCtrl, PpuData, PpuMask, PpuScroll, PpuStatus
from .oam import OamAddr, OamData


class PpuRegisterSet(BusDevice):
    def __init__(self, ppu):
        super().__init__('PPU Register Set')
        self.ppu = ppu
        self.registers = [
            PpuCtrl(),
            PpuMask(),
            PpuStatus(),
            OamAddr(),
            OamData(),
            PpuScroll(),
            PpuAddr(),
            PpuData(),
        ]

    def read(self, addr):
        logical_addr = addr % len(self.registers)
        return self.registers[logical_addr].read()

    def write(self, addr, value):
        logical_addr = addr % len(self.registers)
        self.registers[logical_addr].write(value)
