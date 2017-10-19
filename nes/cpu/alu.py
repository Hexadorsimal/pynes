from .operation import Operation


class AluOperation(Operation):
    def __init__(self, b):
        super().__init__()
        self.b = b

    def execute(self, processor):
        raise NotImplementedError


class AluAddOperation(AluOperation):
    def execute(self, processor):
        a = processor.registers['A']
        b = processor.registers[self.b]
        p = processor.registers['P']
        c = p.flags['C']
        a.data = a.data + b.data + c.data


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
