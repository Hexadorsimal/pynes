class AluParameter:
    def __init__(self, name):
        self.name = name

    def evaluate(self, cpu):
        raise NotImplementedError


class LiteralParameter(AluParameter):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def evaluate(self, cpu):
        return self.value


class RegisterParameter(AluParameter):
    def __init__(self, name):
        super().__init__(name)

    def evaluate(self, cpu):
        return cpu.registers[self.name].contents
