class Instruction:
    def __init__(self, opcode, address_mode, name, cycles, description=None, legal=True):
        self.opcode = opcode
        self.address_mode = address_mode
        self.name = name
        self.description = description
        self.cycles = cycles
        self.legal = legal

    def __repr__(self):
        return "<Instruction {op:02X} {name} {am}>".format(op=self.opcode, name=self.name, am=self.address_mode)

