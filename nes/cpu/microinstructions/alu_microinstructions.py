from nes.alu import Alu
from .microinstruction import Microinstruction


class AluMicroinstruction(Microinstruction):
    def __init__(self, dst, a, b=None):
        super().__init__()
        self.dst = dst
        self.a = a
        self.b = b

    def execute(self, cpu):
        raise NotImplementedError

    @staticmethod
    def process_flags(p, x):
        p.set_flag_value('Z', x == 0)
        p.set_flag_value('N', x & 0x80)


class AluPassthrough(AluMicroinstruction):
    def __init__(self, a):
        super().__init__(dst=a, a=a)

    def __repr__(self):
        return 'ALU_PASS(' + self.a + ')'

    def execute(self, cpu):
        x = cpu.registers[self.a].contents
        self.process_flags(cpu.registers['P'], x)


class Add(AluMicroinstruction):
    def __repr__(self):
        return '{dst} <- {a} + {b} + C'.format(dst=self.dst, a=self.a, b=self.b)

    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        b_input = cpu.registers[self.b].contents
        carry_in = cpu.registers['P'].get_flag_value('C')

        output, carry_out, overflow = Alu.sum(a_input, b_input, carry_in)

        if self.dst:
            cpu.registers[self.dst].contents = output

        cpu.registers['P'].set_flag_value('C', carry_out)
        cpu.registers['P'].set_flag_value('V', overflow)

        self.process_flags(cpu.registers['P'], output)


class Increment(Add):
    def __init__(self, a):
        super().__init__(dst=a, a=a, b='1')

    def __repr__(self):
        return '{dst} <- {a} + 1'.format(dst=self.dst, a=self.a)


class ArithmeticShiftLeft(Add):
    def __init__(self, dst, a):
        super().__init__(dst=dst, a=a, b=a)

    def __repr__(self):
        return '{dst} <- shl {a}'.format(dst=self.dst, a=self.a)


class RotateLeft(AluMicroinstruction):
    def __repr__(self):
        return '{dst} <- rol {a}'.format(dst=self.dst, a=self.a)

    def execute(self, processor):
        pass


class Subtract(AluMicroinstruction):
    def __repr__(self):
        return '{dst} <- {a} - {b}'.format(dst=self.dst, a=self.a, b=self.b)

    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        b_input = cpu.registers[self.b].contents
        carry_in = cpu.registers['P'].get_flag_value('C')

        ones_complement = ~b_input
        twos_complement = ones_complement + 1
        output, carry_out, overflow = Alu.sum(a_input, twos_complement, carry_in)

        if self.dst:
            cpu.registers[self.dst].contents = output

        cpu.registers['P'].set_flag_value('C', carry_out)
        cpu.registers['P'].set_flag_value('V', overflow)

        self.process_flags(cpu.registers['P'], output)


class Decrement(Subtract):
    def __init__(self, a):
        super().__init__(dst=a, a=a, b='1')

    def __repr__(self):
        return '{dst} <- {a} - 1'.format(dst=self.dst, a=self.a)


class Compare(Subtract):
    def __init__(self, a, b):
        super().__init__(dst=None, a=a, b=b)

    def __repr__(self):
        return 'cmp {a} - {b}'.format(a=self.a, b=self.b)


class BitwiseAnd(AluMicroinstruction):
    def __repr__(self):
        return '{dst} <- {a} & {b}'.format(dst=self.dst, a=self.a, b=self.b)

    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        b_input = cpu.registers[self.b].contents

        output = Alu.bitwise_and(a_input, b_input)

        if self.dst:
            cpu.registers[self.dst].contents = output

        self.process_flags(cpu.registers['P'], output)


class BitTest(BitwiseAnd):
    def __init__(self, a, b):
        super().__init__(dst=None, a=a, b=b)

    def __repr__(self):
        return 'test {a} & {b}'.format(dst=self.dst, a=self.a, b=self.b)


class BitwiseOr(AluMicroinstruction):
    def __repr__(self):
        return '{dst} <- {a} | {b}'.format(dst=self.dst, a=self.a, b=self.b)

    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        b_input = cpu.registers[self.b].contents

        output = Alu.bitwise_or(a_input, b_input)

        cpu.registers[self.dst].contents = output

        self.process_flags(cpu.registers['P'], output)


class BitwiseXor(AluMicroinstruction):
    def __repr__(self):
        return '{dst} <- {a} ^ {b}'.format(dst=self.dst, a=self.a, b=self.b)

    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        b_input = cpu.registers[self.b].contents

        output = Alu.bitwise_xor(a_input, b_input)

        cpu.registers[self.dst].contents = output

        self.process_flags(cpu.registers['P'], output)


class LogicalShiftRight(AluMicroinstruction):
    def __repr__(self):
        return '{dst} <- shr {a}'.format(dst=self.dst, a=self.a)

    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents

        output, carry_out = Alu.shift_right(a_input, 0)

        if self.dst:
            cpu.registers[self.dst].contents = output

        cpu.registers['P'].set_flag_value('C', carry_out)

        self.process_flags(cpu.registers['P'], output)


class RotateRight(AluMicroinstruction):
    def __repr__(self):
        return '{dst} <- ror {a}'.format(dst=self.dst, a=self.a)

    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        carry_in = cpu.registers['P'].get_flag_value('C')

        output, carry_out = Alu.shift_right(a_input, carry_in)

        if self.dst:
            cpu.registers[self.dst].contents = output

        cpu.registers['P'].set_flag_value('C', carry_out)

        self.process_flags(cpu.registers['P'], output)
