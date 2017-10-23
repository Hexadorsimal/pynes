from enum import Enum
from ..register import Register


class Alu:
    class Function(Enum):
        sum = 'SUM'
        logical_and = 'AND'
        logical_or = 'OR'
        logical_exclusive_or = 'EOR'
        shift_right = 'SR'

    def __init__(self):
        self.ai = Register('AI', 'A Input Register')
        self.bi = Register('BI', 'B Input Register')
        self.carry_in = 0

        self.output = Register('ADD', 'Adder Hold Register')
        self.overflow = 0
        self.carry_out = 0

    def sum(self):
        self.output.contents = self.ai.contents + self.bi.contents + self.carry_in
        if self.output.contents > 0xff:
            self.carry_out = 1
            self.output.contents &= 0xff

        if (not self.ai.contents & 0x80 and not self.bi.contents & 0x80 and self.output.contents & 0x80) or \
           (self.ai.contents & 0x80 and self.bi.contents & 0x80 and not self.output.contents & 0x80):
            self.overflow = 1
        else:
            self.overflow = 0

    def logical_and(self):
        self.output.contents = self.ai.contents & self.bi.contents
        self.carry_out = self.overflow = 0

    def logical_or(self):
        self.output.contents = self.ai.contents | self.bi.contents
        self.carry_out = self.overflow = 0

    def logical_exclusive_or(self):
        self.output.contents = self.ai.contents ^ self.bi.contents
        self.carry_out = self.overflow = 0

    def shift_right(self):
        if self.ai.contents & 0x01:
            self.carry_out = 1
        else:
            self.carry_out = 0

        self.output.contents = self.ai.contents >> 1

        if self.carry_in:
            self.output.contents |= 0x80

        self.overflow = 0
