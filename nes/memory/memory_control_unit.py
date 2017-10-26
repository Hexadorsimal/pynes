from nes.clock import ClockListener
from nes.ppu import PpuRegisterSet
from . import MemoryMap, AddressRange, Ram


class MemoryControlUnit(ClockListener):
    def __init__(self, nes):
        self.buses = {
            'DB': nes.buses['DB'],
            'AB': nes.buses['AB'],
            'R/W': nes.buses['R/W'],
        }

        self.memory = MemoryMap(0x10000)
        self.memory.add_memory(AddressRange(0x0000, 0x2000), Ram(0x0800))  # RAM
        self.memory.add_memory(AddressRange(0x2000, 0x2000), PpuRegisterSet.create('nes/ppu/ppu.yaml'))  # PPU Registers
        self.memory.add_memory(AddressRange(0x4000, 0x0018), Ram(0x0018))  # APU and IO Registers
        self.memory.add_memory(AddressRange(0x4018, 0x0008), Ram(0x0008))  # Disabled APU and IO functionality

    def clock_event(self, event_name):
        if event_name == 'ab-ready':
            if self.buses['R/W'].get() == 0:
                # Write
                addr = self.buses['AB'].get()
                data = self.buses['DB'].get()
                self.memory.write(addr, data)

            if self.buses['R/W'].get() == 1:
                # Read
                addr = self.buses['AB'].get()
                data = self.memory.read(addr)
                self.buses['DB'].put(data)
