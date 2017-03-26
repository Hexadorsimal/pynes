import os
import yaml
from cpu.connection import Connection
from cpu.counter import Counter
from cpu.flagregister import FlagRegister, StatusFlag
from cpu.instruction import Instruction
from cpu.processor import Processor
from cpu.register import Register


registers = []
connections = []

with open('cpu/6502.yaml', 'r') as stream:
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

instructions = {}

instruction_dir = "cpu/instructions"
instruction_files = os.listdir(instruction_dir)
for filename in instruction_files:
    with open(os.path.join(instruction_dir, filename)) as stream:
        yaml_data = yaml.load(stream)
        for instruction in yaml_data["instructions"]:
            for opcode in instruction["opcodes"]:
                opcode_string = str(opcode["hex"])
                hex_code = int(opcode_string, base=16)
                instructions[hex_code] = Instruction(name=instruction["name"],
                                                     description=instruction["description"],
                                                     opcode=hex_code,
                                                     addressing_mode=opcode["mode"],
                                                     cycles=0)

processor = Processor(registers, connections, instructions)

for register in processor.registers.values():
    print(register)

for (opcode, instruction) in processor.instructions.items():
    print(instruction)
