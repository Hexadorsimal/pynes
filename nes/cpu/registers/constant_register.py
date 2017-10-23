from .register import Register


class ConstantRegister(Register):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.contents = value

    def write(self, addr, data):
        raise RuntimeError('Cannot change the value of a constant register!')
