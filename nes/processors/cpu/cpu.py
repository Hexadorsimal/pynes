from .decoder import Decoder
from ..processor import Processor
from .registers import GeneralPurposeRegister, ProgramCounter, StackPointer, FlagRegister
from .registers.flags import Flag, NegativeFlag, ZeroFlag, OverflowFlag, CarryFlag
from .instructions import InstructionFactory


class Cpu(Processor):
    def __init__(self, bus):
        super().__init__(bus)
        self.registers = {
            'pc': ProgramCounter(),
            'a': GeneralPurposeRegister(),
            'x': GeneralPurposeRegister(),
            'y': GeneralPurposeRegister(),
            'p': FlagRegister({
                'n': NegativeFlag(mask=0x80),
                'v': OverflowFlag(mask=0x40),
                'x': Flag(mask=0x20),
                'b': Flag(mask=0x10),
                'd': Flag(mask=0x08),
                'i': Flag(mask=0x04),
                'z': ZeroFlag(mask=0x02),
                'c': CarryFlag(mask=0x01),
            }),
            's': StackPointer(),
        }

        self.decoder = Decoder()
        self.cycles = 0

    def __repr__(self):
        return 'RICOH 2A03'

    @property
    def pc(self):
        return self.registers['pc']

    @property
    def a(self):
        return self.registers['a']

    @property
    def x(self):
        return self.registers['x']

    @property
    def y(self):
        return self.registers['y']

    @property
    def p(self):
        return self.registers['p']

    @property
    def s(self):
        return self.registers['s']

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
        self.pc.value += instruction.size
        self.execute(instruction)
        super().tick()

    def fetch(self):
        return self.bus.read(self.pc.value)

    def decode(self, opcode):
        info = self.decoder.decode(opcode)
        instruction = InstructionFactory.create(self, info)
        return instruction

    def execute(self, instruction):
        instruction.execute(self)
        self.cycles += instruction.cycles

    def read(self, addr):
        return self.bus.read(addr)

    def write(self, addr, value):
        return self.bus.write(addr, value)

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
        self.bus.write(self.s.pointer, value)
        self.s.value -= 1

    def pull(self):
        self.s.value += 1
        return self.bus.read(self.s.pointer)
