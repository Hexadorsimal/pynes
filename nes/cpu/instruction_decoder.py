from .instructions import all_instructions


class InstructionDecoder:
    def __init__(self):
        self.map = {}

        for instruction in all_instructions:
            self.map[instruction.opcode] = instruction

    def get_instruction(self, opcode):
        return self.map[opcode]
