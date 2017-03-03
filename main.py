import yaml
from src.counter import Counter
from src.processor import Processor
from src.flagregister import FlagRegister, StatusFlag
from src.instruction import Instruction
from src.line import Line


registers = []
lines = []

with open('6502.yaml', 'r') as stream:
    yaml_data = yaml.load(stream)
    for register_dict in yaml_data["registers"]:
        if "flags" in register_dict:
            flags = []
            for flag_dict in register_dict["flags"]:
                flags.append(StatusFlag(**flag_dict))
            register_dict["flags"] = flags
            registers.append(FlagRegister(**register_dict))
        else:
            registers.append(Counter(**register_dict))

    for line_dict in yaml_data["lines"]:
        lines.append(Line(**line_dict))

instructions = []

with open('instructions.yaml') as stream:
    yaml_data = yaml.load(stream)
    for instruction_dict in yaml_data["instructions"]:
        for variation_dict in instruction_dict["variations"]:
            instructions.append(Instruction(name=instruction_dict["name"], **variation_dict))


processor = Processor(registers, lines, instructions)

for register in processor.registers.values():
    print(register)

for line in processor.lines.values():
    print(line)

for (opcode, instruction) in processor.instructions.items():
    print(instruction)
