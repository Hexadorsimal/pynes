from .instructions import all_instructions


class InstructionDecoder:
    def __init__(self):
        self.map = {}

        for inst_type in all_instructions:
            instruction = inst_type()
            self.map[instruction.opcode] = instruction

    def get_instruction(self, opcode):
        return self.map[opcode]
