class Processor:
    def __init__(self, registers, instructions):
        self.registers = {}
        for register in registers:
            self.registers[register.name] = register

        self.instructions = {}
        for instruction in instructions:
            self.instructions[instruction.opcode] = instruction
