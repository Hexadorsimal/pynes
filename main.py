from src.counter import Counter
from src.processor import Processor
from src.register import Register
from src.flagregister import FlagRegister, StatusFlag
from src.instruction import Instruction
from src.addressmode import AddressMode


flags = [
    StatusFlag("C", "Carry", 0x01, "Set if the add produced a carry, or if the subtraction produced a borrow.  Also holds bits after a logical shift."),
    StatusFlag("Z", "Zero", 0x02, "Set if the result of the last operation (load/inc/dec/add/sub) was zero."),
    StatusFlag("I", "Interrupt", 0x04, "Set if maskable interrupts are disabled."),
    StatusFlag("D", "Decimal", 0x08, "Set if decimal mode active.(NES unused)"),
    StatusFlag("B", "Breakpoint", 0x10, "Set if an interrupt caused by a BRK, reset if caused by an external interrupt."),
    StatusFlag("R", "Reserved", 0x20, "Should always be 1"),
    StatusFlag("O", "Overflow", 0x40, "Set if the addition of two like-signed numbers or the subtraction of two unlike-signed numbers produces a result greater than +127 or less than -128."),
    StatusFlag("S", "Sign", 0x80, "Set if bit 7 of the Accumulator is set")
]

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
