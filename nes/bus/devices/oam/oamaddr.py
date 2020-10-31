from nes.processors.cpu.registers import Register


class OamAddr(Register):
    def __init__(self, data=0):
        self.data = data

    def read(self):
        raise RuntimeError('OAMADDR is a write-only register')

    def write(self, data):
        self.data = data
