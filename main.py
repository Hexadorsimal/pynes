from src.processor import Processor
from src.register import Register
from src.statusregister import StatusRegister


registers = [
    Register("PC", "Program Counter", 16),
    Register("A", "Accumulator", 8),
    Register("X", "X Index", 8),
    Register("Y", "Y Index", 8),
    Register("SP", "Stack Pointer", 8),
    StatusRegister("P", "Processor Status", 8),
]

processor = Processor(registers)

for (name, register) in processor.registers.items():
    print(register)
