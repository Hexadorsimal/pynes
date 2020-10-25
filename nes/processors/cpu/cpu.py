from enum import Enum
from .decoder import Decoder
from ..processor import Processor
from nes.registers import Register
from nes.flags import Flag, NFlag, ZFlag
from nes.processors.cpu.instructions.factory import InstructionFactory


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
        return self.bus.read(self.pc)

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

    def compare(self, a, b):
        self.update_zn(a - b)
        if a >= b:
            self.c = 1
        else:
            self.c = 0

    @staticmethod
    def pages_differ(a, b):
        return a & 0xFF00 != b & 0xFF00

    def bcc(self, address):
        if self.c == 0:
            self.pc = address
            return True
        else:
            return False

    def bcs(self, address):
        if self.c != 0:
            self.pc = address
            return True
        else:
            return False

    def beq(self, address):
        if self.z != 0:
            self.pc = address
            return True
        else:
            return False

    def bit(self, address):
        value = self.bus.read(address)
        self.v = (value >> 6) & 0x01
        self.update_z(value & self.a)
        self.update_n(value)

    def bmi(self, address):
        if self.n != 0:
            self.pc = address
            return True
        else:
            return False

    def bne(self, address):
        if self.z == 0:
            self.pc = address
            return True
        else:
            return False

    def bpl(self, address):
        if self.n == 0:
            self.pc = address
            return True
        else:
            return False

    def brk(self, address):
        self.push16(self.pc)
        self.php(address)
        self.sei(address)
        self.pc = self.bus.read16(0xfffe)

    def bvc(self, address):
        if self.v == 0:
            self.pc = address
            return True
        else:
            return False

    def bvs(self, address):
        if self.v != 0:
            self.pc = address
            return True
        else:
            return False

    def clc(self, address):
        self.c = 0

    def cld(self, address):
        self.d = 0

    def cli(self, address):
        self.i = 0

    def clv(self, address):
        self.v = 0

    def cmp(self, address):
        value = self.bus.read(address)
        self.compare(self.a, value)

    def cpx(self, address):
        value = self.bus.read(address)
        self.compare(self.x, value)

    def cpy(self, address):
        value = self.bus.read(address)
        self.compare(self.y, value)

    def dec(self, address):
        value = self.bus.read(address) - 1
        self.bus.write(address, value)
        self.update_zn(value)

    def dex(self, address):
        self.x -= 1
        self.update_zn(self.x)

    def dey(self, address):
        self.y -= 1
        self.update_zn(self.y)

    def eor(self, address):
        self.a = self.a ^ self.bus.read(address)
        self.update_zn(self.a)

    def inc(self, address):
        value = self.bus.read(address) + 1
        self.bus.write(address, value)
        self.update_zn(value)

    def inx(self, address):
        self.x += 1
        self.update_zn(self.x)

    def iny(self, address):
        self.y += 1
        self.update_zn(self.y)

    def jmp(self, address):
        self.pc = address

    def jsr(self, address):
        self.push16(self.pc - 1)
        self.pc = address

    def lda(self, address):
        self.a = self.bus.read(address)
        self.update_zn(self.a)

    def ldx(self, address):
        self.x = self.bus.read(address)
        self.update_zn(self.x)

    def ldy(self, address):
        self.y = self.bus.read(address)
        self.update_zn(self.y)

    def lsr(self, address):
        if address == 'Accumulator':
            self.c = self.a & 0x01
            self.a >>= 1
            self.update_zn(self.a)
        else:
            value = self.bus.read(address)
            self.c = value & 0x01
            value >>= 1
            self.bus.write(address, value)
            self.update_zn(value)

    def nop(self, address):
        pass

    def ora(self, address):
        self.a |= self.bus.read(address)
        self.update_zn(self.a)

    def pha(self, address):
        self.push(self.a)

    def php(self, address):
        self.push(self.p)

    def pla(self, address):
        self.a = self.pull()
        self.update_zn(self.a)

    def plp(self, address):
        self.p = self.pull()

    def rol(self, address):
        if address == 'Accumulator':
            c = self.c
            self.c = (self.a >> 7) & 0x01
            self.a = (self.a << 1) | c
            self.update_zn(self.a)
        else:
            c = self.c
            value = self.bus.read(address)
            self.c = (value >> 7) & 0x01
            value = (value << 1) | c
            self.bus.write(address, value)
            self.update_zn(value)

    def ror(self, address):
        if address == 'Accumulator':
            c = self.c
            self.c = self.a & 0x01
            self.a = (self.a >> 1) | (c << 7)
            self.update_zn(self.a)
        else:
            c = self.c
            value = self.bus.read(address)
            self.c = value & 0x01
            value = (value >> 1) | (c << 7)
            self.bus.write(address, value)
            self.update_zn(value)

    def rti(self, address):
        self.p = self.pull()
        self.pc = self.pull16()

    def rts(self, address):
        self.pc = self.pull16() + 1

    def sbc(self, address):
        a = self.a
        b = self.bus.read(address)
        c = self.c
        self.a = a - b - (1 - c)
        self.update_zn(self.a)
        if a - b - (1 - c) > 0:
            self.c = 1
        else:
            self.c = 0

        if (a ^ b) & 0x80 != 0 and (a ^ self.a) & 0x80 != 0:
            self.v = 1
        else:
            self.v = 0

    def sec(self, address):
        self.c = 1

    def sed(self, address):
        self.d = 1

    def sei(self, address):
        self.i = 1

    def sta(self, address):
        self.bus.write(address, self.a)

    def stx(self, address):
        self.bus.write(address, self.x)

    def sty(self, address):
        self.bus.write(address, self.y)

    def tax(self, address):
        self.x = self.a
        self.update_zn(self.x)

    def tay(self, address):
        self.y = self.a
        self.update_zn(self.y)

    def tsx(self, address):
        self.x = self.s
        self.update_zn(self.x)

    def txa(self, address):
        self.a = self.x
        self.update_zn(self.a)

    def txs(self, address):
        self.s = self.x

    def tya(self, address):
        self.a = self.y
        self.update_zn(self.a)
