class Processor:
    def __init__(self, registers, connections, instructions):
        self.registers = {}
        for register in registers:
            self.registers[register.name] = register

        self.connections = {}
        for connection in connections:
            self.connections[connection.name] = connection

        self.instructions = {}
        for instruction in instructions:
            self.instructions[instruction.opcode] = instruction
