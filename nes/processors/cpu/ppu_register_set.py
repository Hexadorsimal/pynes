from nes.bus import BusDevice
from nes.processors.ppu.registers.ppuctrl import PpuCtrl
from nes.processors.ppu.registers.ppumask import PpuMask
from nes.processors.ppu.registers.ppustatus import PpuStatus
from nes.processors.ppu.registers.ppuscroll import PpuScroll
from nes.processors.ppu.registers.ppuaddr import PpuAddr
from nes.processors.ppu.registers.ppudata import PpuData
from nes.processors.ppu.registers.oamaddr import OamAddr
from nes.processors.ppu.registers.oamdata import OamData


class PpuRegisterSet(BusDevice):
    def __init__(self, ppu):
        super().__init__('ppu register set')
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
