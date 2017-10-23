from nes.alu import Alu
from .operation import Operation


class AluOperation(Operation):
    def __init__(self, dst, a, b=None):
        super().__init__()
        self.dst = dst
        self.a = a
        self.b = b

    def execute(self, cpu):
        raise NotImplementedError


class AddOperation(AluOperation):
    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        b_input = cpu.registers[self.b].contents
        carry_in = cpu.registers['P'].get_flag_value('C')

        output, carry_out, overflow = Alu.sum(a_input, b_input, carry_in)

        if self.dst:
            cpu.registers[self.dst].contents = output

        cpu.registers['P'].set_flag_value('C', carry_out)
        cpu.registers['P'].set_flag_value('V', overflow)
        cpu.registers['P'].set_flag_value('Z', output == 0)
        cpu.registers['P'].set_flag_value('N', output & 0x80)


class IncrementOperation(AddOperation):
    def __init__(self, a):
        super().__init__(dst=a, a=a, b='1')


class ArithmeticShiftLeftOperation(AddOperation):
    def __init__(self, dst, a):
        super().__init__(dst=dst, a=a, b=a)


class RotateLeftOperation(AluOperation):
    def execute(self, processor):
        pass


class SubtractOperation(AluOperation):
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
        cpu.registers['P'].set_flag_value('Z', output == 0)
        cpu.registers['P'].set_flag_value('N', output & 0x80)


class DecrementOperation(SubtractOperation):
    def __init__(self, a):
        super().__init__(dst=a, a=a, b='1')


class CompareOperation(SubtractOperation):
    def __init__(self, a, b):
        super().__init__(dst=None, a=a, b=b)


class BitwiseAndOperation(AluOperation):
    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        b_input = cpu.registers[self.b].contents

        output = Alu.bitwise_and(a_input, b_input)

        if self.dst:
            cpu.registers[self.dst].contents = output

        cpu.registers['P'].set_flag_value('Z', output == 0)
        cpu.registers['P'].set_flag_value('N', output & 0x80)


class BitTestOperation(BitwiseAndOperation):
    def __init__(self, a, b):
        super().__init__(dst=None, a=a, b=b)


class BitwiseOrOperation(AluOperation):
    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        b_input = cpu.registers[self.b].contents

        output = Alu.bitwise_or(a_input, b_input)

        cpu.registers[self.dst].contents = output
        cpu.registers['P'].set_flag_value('Z', output == 0)
        cpu.registers['P'].set_flag_value('N', output & 0x80)


class BitwiseXOrOperation(AluOperation):
    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        b_input = cpu.registers[self.b].contents

        output = Alu.bitwise_xor(a_input, b_input)

        cpu.registers[self.dst].contents = output
        cpu.registers['P'].set_flag_value('Z', output == 0)
        cpu.registers['P'].set_flag_value('N', output & 0x80)


class LogicalShiftRightOperation(AluOperation):
    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents

        output, carry_out = Alu.shift_right(a_input, 0)

        if self.dst:
            cpu.registers[self.dst].contents = output

        cpu.registers['P'].set_flag_value('C', carry_out)
        cpu.registers['P'].set_flag_value('Z', output == 0)
        cpu.registers['P'].set_flag_value('N', output & 0x80)


class RotateRightOperation(AluOperation):
    def execute(self, cpu):
        a_input = cpu.registers[self.a].contents
        carry_in = cpu.registers['P'].get_flag_value('C')

        output, carry_out = Alu.shift_right(a_input, carry_in)

        if self.dst:
            cpu.registers[self.dst].contents = output

        cpu.registers['P'].set_flag_value('C', carry_out)
        cpu.registers['P'].set_flag_value('Z', output == 0)
        cpu.registers['P'].set_flag_value('N', output & 0x80)
