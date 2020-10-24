from nes.bus import BusDevice
from nes.registers.ppu import PpuCtrl, PpuMask, PpuStatus, PpuScroll, PpuAddr, PpuData
from nes.registers.oam import OamAddr, OamData


class PpuRegisterSet(BusDevice):
    def __init__(self, ppu):
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

    @property
    def name(self):
        return 'ppu register set'

    def read(self, addr):
        logical_addr = addr % len(self.registers)
        return self.registers[logical_addr].read()

    def write(self, addr, value):
        logical_addr = addr % len(self.registers)
        self.registers[logical_addr].write(value)
