class Instruction:
    def __init__(self, opcode, addressing_mode, name, cycles, description, legal=True):
        self.opcode = opcode
        self.addressing_mode = addressing_mode
        self.name = name
        self.description = description
        self.cycles = cycles
        self.legal = legal

    def __repr__(self):
        return "<Instruction {op:02X} {name} {am}>".format(op=self.opcode, name=self.name, am=self.addressing_mode)

