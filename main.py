import yaml
from src.counter import Counter
from src.processor import Processor
from src.register import Register
from src.flagregister import FlagRegister, StatusFlag
from src.instruction import Instruction
from src.addressmode import AddressMode


registers = []

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

instructions = [
    Instruction(0, AddressMode.accumulator, "ADC", "Add memory to accumulator with carry", True)
]

processor = Processor(registers, instructions)

for (name, register) in processor.registers.items():
    print(register)

for (opcode, instruction) in processor.instructions.items():
    print(instruction)
