from nes.bus import BusDevice
from nes.registers.general_register import GeneralRegister
from nes.registers.apu import Sq1Hi, Sq1Lo, Sq1Sweep, Sq1Vol, Sq2Hi, Sq2Lo, Sq2Sweep, Sq2Vol, TriLinear, TriHi, TriLo, NoiseHi, NoiseLo, NoiseVol, DmcRaw, DmcFreq, DmcStart, DmcLen, SndChn
from nes.registers.oam import OamDma
from nes.registers.joy import Joy1, Joy2


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
            GeneralRegister(),
            TriLo(),
            TriHi(),
            NoiseVol(),
            GeneralRegister(),
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
            GeneralRegister(),
            GeneralRegister(),
            GeneralRegister(),
            GeneralRegister(),
            GeneralRegister(),
            GeneralRegister(),
            GeneralRegister(),
            GeneralRegister(),
        ]

    @property
    def name(self):
        return 'apu io register set'

    def read(self, addr):
        logical_addr = addr % len(self.registers)
        return self.registers[logical_addr].read()

    def write(self, addr, value):
        logical_addr = addr % len(self.registers)
        self.registers[logical_addr].write(value)
