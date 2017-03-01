from .register import Register


class Processor:
    def __init__(self, registers):
        self.registers = {}

        for register in registers:
            self.registers[register.name] = register

