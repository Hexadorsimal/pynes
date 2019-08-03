from .register import Register


class OamAddr(Register):
    def __init__(self, data=0):
        self.data = data

    def write(self, data):
        self.data = data
