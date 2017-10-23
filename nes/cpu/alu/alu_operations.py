from ..operation import Operation


class AluOperation(Operation):
    def __init__(self, dst, a, b=None):
        super().__init__()
        self.dst = dst
        self.a = a
        self.b = b

    def execute(self, cpu):
        raise NotImplementedError


class AluIncrementOperation(AluOperation):
    def __init__(self, a):
        super().__init__(a, a)

    def execute(self, cpu):
        dst = cpu.registers[self.dst]
        a = cpu.registers[self.a]
        p = cpu.registers['P']

        dst.contents = a.contents + 1
        if dst.contents > 0xff:
            dst.contents = 0
            p.set_flag('V')
        else:
            p.clear_flag('V')

        if dst.contents == 0:
            p.set_flag('Z')
        else:
            p.clear_flag('Z')

        if dst.contents & 0x80:
            p.set_flag('N')
        else:
            p.clear_flag('N')


class AluDecrementOperation(AluIncrementOperation):
    pass


class AluAddOperation(AluOperation):
    def execute(self, cpu):
        acc = cpu.registers['A']
        p = cpu.registers['P']

        a = self.a.evaluate(cpu)
        b = self.b.evaulate(cpu)

        acc.contents = a + b + p.get_flag_value['C']


class AluSubtractOperation(AluOperation):
    def execute(self, processor):
        pass


class AluLogicalAndOperation(AluOperation):
    def execute(self, processor):
        pass


class AluLogicalOrOperation(AluOperation):
    def execute(self, processor):
        pass


class AluExclusiveOrOperation(AluOperation):
    def execute(self, execute):
        pass


class AluArithmeticShiftLeftOperation(AluOperation):
    def execute(self, processor):
        pass


class AluLogicalShiftRightOperation(AluOperation):
    def execute(self, processor):
        pass


class AluRotateLeftOperation(AluOperation):
    def execute(self, processor):
        pass


class AluRotateRightOperation(AluOperation):
    def execute(self, processor):
        pass
