from .instructions import all_instructions


class InstructionDecoder:
    def __init__(self):
        self.map = {}

        for inst_type in all_instructions:
            instruction = inst_type()
            for opcode, addressing_mode in instruction.addressing_modes.items():
                self.map[opcode] = instruction

    def get_instruction(self, opcode):
        return self.map[opcode]

    def get_addressing_mode(self, opcode):
        instruction = self.get_instruction(opcode)
        return instruction.addressing_modes[opcode]()
