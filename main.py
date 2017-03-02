import yaml
from src.counter import Counter
from src.processor import Processor
from src.register import Register
from src.flagregister import FlagRegister, StatusFlag
from src.instruction import Instruction
from src.addressmode import AddressMode


flags = []

with open('flags.yaml', 'r') as stream:
    yaml_data = yaml.load(stream)
    for flag_dict in yaml_data["flags"]:
        flags.append(StatusFlag(**flag_dict))

registers = [
    Counter("PC", "Program Counter", 16),
    Register("A", "Accumulator", 8),
    Register("X", "X Index", 8),
    Register("Y", "Y Index", 8),
    Counter("SP", "Stack Pointer", 8),
    FlagRegister(flags, "P", "Processor Status", 8),
]

instructions = [
    Instruction(0, AddressMode.accumulator, "ADC", "Add memory to accumulator with carry", True)
]

processor = Processor(registers, instructions)

for (name, register) in processor.registers.items():
    print(register)

for (opcode, instruction) in processor.instructions.items():
    print(instruction)
