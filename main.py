import yaml
from src.addressingmode import AddressingMode
from src.connection import Connection
from src.counter import Counter
from src.flagregister import FlagRegister, StatusFlag
from src.instruction import Instruction
from src.processor import Processor
from src.register import Register


registers = []
connections = []

with open('6502.yaml', 'r') as stream:
    yaml_data = yaml.load(stream)
    for register_dict in yaml_data["registers"]:
        type = register_dict.pop("type", None)
        if type == "flags":
            flags = []
            for flag_dict in register_dict["flags"]:
                flags.append(StatusFlag(**flag_dict))
            register_dict["flags"] = flags
            registers.append(FlagRegister(**register_dict))
        elif type == "accumulator" or type == "index":
            registers.append(Counter(**register_dict))
        else:
            registers.append(Register(**register_dict))

    for connection_dict in yaml_data["connections"]:
        connections.append(Connection(**connection_dict))

instructions = []
addressing_modes = []

with open('instructions.yaml') as stream:
    yaml_data = yaml.load(stream)
    for addressing_mode_dict in yaml_data["addressing_modes"]:
        addressing_modes.append(AddressingMode(**addressing_mode_dict))
    for instruction_dict in yaml_data["instructions"]:
        for variation_dict in instruction_dict["variations"]:
            instructions.append(Instruction(name=instruction_dict["name"], **variation_dict))


processor = Processor(registers, connections, instructions)

for register in processor.registers.values():
    print(register)

for line in processor.lines.values():
    print(line)

for (opcode, instruction) in processor.instructions.items():
    print(instruction)
