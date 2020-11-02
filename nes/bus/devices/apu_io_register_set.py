from nes.bus import BusDevice
from nes.processors.registers import Register
from .apu import Sq1Hi, Sq1Lo, Sq1Sweep, Sq1Vol, Sq2Hi, Sq2Lo, Sq2Sweep, Sq2Vol, TriLinear, TriHi, TriLo, NoiseHi, NoiseLo, NoiseVol, DmcRaw, DmcFreq, DmcStart, DmcLen, SndChn
from nes.processors.ppu.registers import OamDma
from .joy import Joy1, Joy2


class ApuIoRegisterSet(BusDevice):
    def __init__(self):
        self.registers = [
            Sq1Vol(),
            Sq1Sweep(),
            Sq1Lo(),
            Sq1Hi(),
            Sq2Vol(),
            Sq2Sweep(),
            Sq2Lo(),
            Sq2Hi(),
            TriLinear(),
            Register(),
            TriLo(),
            TriHi(),
            NoiseVol(),
            Register(),
            NoiseLo(),
            NoiseHi(),
            DmcFreq(),
            DmcRaw(),
            DmcStart(),
            DmcLen(),
            OamDma(),
            SndChn(),
            Joy1(),
            Joy2(),
            Register(),
            Register(),
            Register(),
            Register(),
            Register(),
            Register(),
            Register(),
            Register(),
        ]

    def read(self, addr):
        logical_addr = addr % len(self.registers)
        return self.registers[logical_addr].read()

    def write(self, addr, value):
        logical_addr = addr % len(self.registers)
        self.registers[logical_addr].write(value)
