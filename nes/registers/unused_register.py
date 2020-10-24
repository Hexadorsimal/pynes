from .register import Register


class UnusedRegister(Register):
    def __init__(self):
        self.value = 0

    def read(self):
        return self.value

    def write(self, value):
        self.value = value
