class Instruction:
    def __init__(self, opcode, address_mode, name, cycle_count, description=None, legal=True):
        self.opcode = opcode
        self.address_mode = address_mode
        self.name = name
        self.description = description
        self.cycle_count = cycle_count
        self.legal = legal

    def __repr__(self):
        return "<Instruction {op:02X} {name} {am}>".format(op=self.opcode, name=self.name, am=self.address_mode)
