class Processor:
    def __init__(self, registers, lines, instructions):
        self.registers = {}
        for register in registers:
            self.registers[register.name] = register

        self.lines = {}
        for line in lines:
            self.lines[line.name] = line

        self.instructions = {}
        for instruction in instructions:
            self.instructions[instruction.opcode] = instruction
