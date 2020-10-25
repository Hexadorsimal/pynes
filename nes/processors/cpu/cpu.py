from enum import Enum
from .decoder import Decoder
from ..processor import Processor
from nes.registers import Register
from nes.flags import Flag, NFlag, ZFlag
from nes.instructions import InstructionFactory


class Cpu(Processor):
    class Flags(Enum):
        negative_result = 0x80
        overflow = 0x40
        expansion = 0x20
        break_command = 0x10
        decimal_mode = 0x08
        interrupt_disable = 0x04
        zero_result = 0x02
        carry = 0x01

    def __init__(self, bus):
        super().__init__(bus)
        self.registers = {
            'pc': Register(),
            'a': Register(),
            'x': Register(),
            'y': Register(),
            'p': Register(),
            's': Register(),
        }

        self.flags = {
            'n': NFlag(),
            'v': Flag(),
            'x': Flag(),
            'b': Flag(),
            'd': Flag(),
            'i': Flag(),
            'z': ZFlag(),
            'c': Flag(),
        }

        self.decoder = Decoder()
        self.cycles = 0

    def power_on(self):
        self.registers['pc'].set(0xC000)
        self.registers['s'].set(0xFD)
        self.registers['p'].set(0x24)

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
        pc = self.registers.get('pc')
        return self.bus.read(pc.get())

    def decode(self, opcode):
        info = self.decoder.decode(opcode)
        return InstructionFactory.create(self, info)

    def execute(self, instruction):
        self.pc += instruction.size

        instruction.execute()

        self.cycles += instruction.cycles

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
        self.bus.write(0x0100 | self.s, value)
        self.s = (self.s - 1) & 0x00ff

    def pull(self):
        self.s = (self.s + 1) & 0x00ff
        return self.bus.read(0x0100 | self.s)

    def push16(self, value):
        hi = value >> 8
        lo = value & 0x00ff
        self.push(hi)
        self.push(lo)

    def pull16(self):
        lo = self.pull()
        hi = self.pull()
        return hi << 8 | lo
