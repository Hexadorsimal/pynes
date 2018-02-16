from enum import Enum


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

    def __init__(self, nes):
        self.pc = 0
        self.a = 0
        self.x = 0
        self.y = 0
        self.p = 0
        self.s = 0

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

    @property
    def b(self):
        return self.get_flag(self.Flags.break_command.value)

    @b.setter
    def b(self, value):
        self.set_flag(self.Flags.break_command.value, value)

    @property
    def c(self):
        return self.set_flag(self.Flags.carry.value)

    @c.setter
    def c(self, value):
        self.set_flag(self.Flags.carry.value, value)

    @property
    def d(self):
        return self.get_flag(self.Flags.decimal_mode.value)

    @d.setter
    def d(self, value):
        self.set_flag(self.Flags.decimal_mode.value, value)

    @property
    def i(self):
        return self.get_flag(self.Flags.interrupt_disable.value)

    @i.setter
    def i(self, value):
        self.set_flag(self.Flags.interrupt_disable.value, value)

    @property
    def n(self):
        return self.get_flag(self.Flags.negative_result.value)

    @n.setter
    def n(self, value):
        self.set_flag(self.Flags.negative_result.value, value)

    @property
    def v(self):
        self.get_flag(self.Flags.overflow.value)

    @v.setter
    def v(self, value):
        self.set_flag(self.Flags.overflow.value, value)

    @property
    def z(self):
        return self.get_flag(self.Flags.zero_result.value)

    @z.setter
    def z(self, value):
        self.set_flag(self.Flags.zero_result.value, value)

    def power_on(self):
        self.pc = 0xC000
        self.s = 0xFD
        self.p = 0x24
        self.fetch()

    def reset(self):
        # read mem from RESET_LO, put in PCL
        # read mem from RESET_HI, put in PCH
        pass

    def irq(self):
        pass

    def nmi(self):
        pass

    def fetch(self):
        pass

    def decode(self):
        opcode = self.readmem(self.pc)
        instruction = self.decoder.get_instruction(opcode)
        addressing_mode = self.decoder.get_addressing_mode(opcode)
