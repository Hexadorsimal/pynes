from .decoder import Decoder
from ..processor import Processor
from nes.registers import GeneralPurposeRegister, ProgramCounter, StackPointer, FlagRegister, Flag
from nes.instructions import InstructionFactory


class Cpu(Processor):
    def __init__(self, bus):
        super().__init__(bus)
        self.registers = {
            'pc': ProgramCounter(mask=0xffff),
            'a': GeneralPurposeRegister(),
            'x': GeneralPurposeRegister(),
            'y': GeneralPurposeRegister(),
            'p': FlagRegister({
                'n': Flag(mask=0x80),
                'v': Flag(mask=0x40),
                'x': Flag(mask=0x20),
                'b': Flag(mask=0x10),
                'd': Flag(mask=0x08),
                'i': Flag(mask=0x04),
                'z': Flag(mask=0x02),
                'c': Flag(mask=0x01),
            }),
            's': StackPointer(page=0x0100),
        }

        self.decoder = Decoder()
        self.cycles = 0

    def __getattr__(self, item):
        if item in self.registers:
            return self.registers[item]
        elif item in self.p:
            return self.p[item]

    def power_on(self):
        self.pc.value = 0xC000
        self.s.value = 0xFD
        self.p.value = 0x24

    def reset(self):
        # read mem from RESET_LO, put in PCL
        # read mem from RESET_HI, put in PCH
        pass

    def irq(self):
        pass

    def nmi(self):
        pass

    def tick(self):
        opcode = self.fetch()
        instruction = self.decode(opcode)
        self.execute(instruction)
        super().tick()

    def fetch(self):
        return self.bus.read(self.pc.value)

    def decode(self, opcode):
        info = self.decoder.decode(opcode)
        return InstructionFactory.create(self, info)

    def execute(self, instruction):
        self.pc += instruction.size

        instruction.execute()

        self.cycles += instruction.cycles

    def read8(self, addr):
        return self.bus.read(addr)

    def read16(self, addr):
        lo = self.bus.read(addr)
        hi = self.bus.read(addr + 1)
        return (hi << 8) | lo

    def read16_bug(self, addr):
        a = addr
        b = (a & 0xff00) | ((a & 0x00ff) + 1)
        lo = self.bus.read(a)
        hi = self.bus.read(b)
        return (hi << 8) | lo

    def push(self, value):
        self.bus.write(self.s.addr, value)
        self.s -= 1

    def pull(self):
        self.s += 1
        return self.bus.read(self.s.addr)

    def push16(self, value):
        hi = (value & 0xff00) >> 8
        lo = value & 0x00ff
        self.push(hi)
        self.push(lo)

    def pull16(self):
        lo = self.pull()
        hi = self.pull()
        return hi << 8 | lo
