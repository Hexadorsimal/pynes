from enum import Enum
from .decoder import Decoder


class Cpu:
    class Flags(Enum):
        negative_result = 0x80
        overflow = 0x40
        expansion = 0x20
        break_command = 0x10
        decimal_mode = 0x08
        interrupt_disable = 0x04
        zero_result = 0x02
        carry = 0x01

    def __init__(self, memory):
        self.pc = 0
        self.a = 0
        self.x = 0
        self.y = 0
        self.p = 0
        self.s = 0
        self.memory = memory
        self.decoder = Decoder()
        self.cycles = 0

    def get_flag(self, flag):
        if self.p & flag:
            return 1
        else:
            return 0

    def set_flag(self, flag, value):
        if value:
            self.p |= flag
        else:
            self.p &= ~flag

    def update_zn(self, value):
        self.update_z(value)
        self.update_n(value)

    def update_z(self, value):
        if value == 0:
            self.z = 1
        else:
            self.z = 0

    def update_n(self, value):
        if value & 0x80:
            self.n = 1
        else:
            self.n = 0

    @property
    def b(self):
        return self.get_flag(Cpu.Flags.break_command.value)

    @b.setter
    def b(self, value):
        self.set_flag(Cpu.Flags.break_command.value, value)

    @property
    def c(self):
        return self.set_flag(Cpu.Flags.carry.value)

    @c.setter
    def c(self, value):
        self.set_flag(Cpu.Flags.carry.value, value)

    @property
    def d(self):
        return self.get_flag(Cpu.Flags.decimal_mode.value)

    @d.setter
    def d(self, value):
        self.set_flag(Cpu.Flags.decimal_mode.value, value)

    @property
    def i(self):
        return self.get_flag(Cpu.Flags.interrupt_disable.value)

    @i.setter
    def i(self, value):
        self.set_flag(Cpu.Flags.interrupt_disable.value, value)

    @property
    def n(self):
        return self.get_flag(Cpu.Flags.negative_result.value)

    @n.setter
    def n(self, value):
        self.set_flag(Cpu.Flags.negative_result.value, value)

    @property
    def v(self):
        self.get_flag(Cpu.Flags.overflow.value)

    @v.setter
    def v(self, value):
        self.set_flag(Cpu.Flags.overflow.value, value)

    @property
    def z(self):
        return self.get_flag(Cpu.Flags.zero_result.value)

    @z.setter
    def z(self, value):
        self.set_flag(Cpu.Flags.zero_result.value, value)

    def power_on(self):
        self.pc = 0xC000
        self.s = 0xFD
        self.p = 0x24

        while True:
            self.step()

    def reset(self):
        # read mem from RESET_LO, put in PCL
        # read mem from RESET_HI, put in PCH
        pass

    def irq(self):
        pass

    def nmi(self):
        pass

    def step(self):
        opcode = self.fetch()
        instruction = self.decode(opcode)
        self.execute(instruction)

    def fetch(self):
        return self.memory.read(self.pc)

    def decode(self, opcode):
        return self.decoder.decode(opcode)

    def execute(self, instruction):
        mode = instruction['addressing_mode']
        address = 0
        page_crossed = False

        if mode == 'Absolute':
            address = self.read16(self.pc + 1)
        elif mode == 'AbsoluteX':
            address = self.read16(self.pc + 1) + self.x
            page_crossed = self.pages_differ(address - self.x, address)
        elif mode == 'AbsoluteY':
            address = self.read16(self.pc + 1) + self.y
            page_crossed = self.pages_differ(address - self.y, address)
        elif mode == 'Accumulator':
            address = 0
        elif mode == 'Immediate':
            address = self.pc + 1
        elif mode == 'Implied':
            address = 0
        elif mode == 'IndexedIndirect':
            address = self.read16_bug(self.memory.read(self.pc + 1) + self.x)
        elif mode == 'Indirect':
            address = self.read16_bug(self.read16(self.pc + 1))
        elif mode == 'IndirectIndexed':
            address = self.read16_bug(self.memory.read(self.pc + 1)) + self.y
        elif mode == 'Relative':
            offset = self.memory.read(self.pc + 1)
            if offset < 0x80:
                address = self.pc + 2 + offset
            else:
                address = self.pc + 2 + offset - 0x100
        elif mode == 'ZeroPage':
            address = self.memory.read(self.pc + 1)
        elif mode == 'ZeroPageX':
            address = (self.memory.read(self.pc + 1) + self.x) & 0xff
        elif mode == 'ZeroPageY':
            address = (self.memory.read(self.pc + 1) + self.y) & 0xff

        self.pc += instruction['size']

        cycles = instruction['cycles']
        if page_crossed:
            cycles += instruction['page_cycles']

        self.cycles += cycles

        instr = instruction['name'].lower()
        getattr(self, instr)(address)

        return cycles

    def read16(self, addr):
        lo = self.memory.read(addr)
        hi = self.memory.read(addr + 1)
        return (hi << 8) | lo

    def read16_bug(self, addr):
        a = addr
        b = (a & 0xff00) | ((a & 0x00ff) + 1)
        lo = self.memory.read(a)
        hi = self.memory.read(b)
        return (hi << 8) | lo

    @staticmethod
    def pages_differ(a, b):
        return a & 0xFF00 != b & 0xFF00

    def jmp(self, address):
        self.pc = address

    def ldx(self, address):
        self.x = self.memory.read(address)
        self.update_zn(self.x)

    def stx(self, address):
        self.memory.write(address, self.x)
