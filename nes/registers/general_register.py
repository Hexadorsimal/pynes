from .register import Register


class GeneralRegister(Register):
    def __init__(self):
        self.value = 0

    def get(self):
        return self.value

    def set(self, value):
        self.value = value
