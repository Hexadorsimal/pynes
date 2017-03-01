class Instruction:
    def __init__(self, opcode, address_mode, name, description, is_legal):
        self.opcode = opcode
        self.address_mode = address_mode
        self.name = name
        self.description = description
        self.is_legal = is_legal

    def __repr__(self):
        return "<Instruction {op} {name} {am}>".format(op=self.opcode, name=self.name, am=self.address_mode.value)
