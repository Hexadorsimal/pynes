from src.processor import Processor
from src.register import Register
from src.flagregister import FlagRegister, StatusFlag


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
    Register("PC", "Program Counter", 16),
    Register("A", "Accumulator", 8),
    Register("X", "X Index", 8),
    Register("Y", "Y Index", 8),
    Register("SP", "Stack Pointer", 8),
    FlagRegister(flags, "P", "Processor Status", 8),
]

processor = Processor(registers)

for (name, register) in processor.registers.items():
    print(register)
