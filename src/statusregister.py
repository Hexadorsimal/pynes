from enum import Enum
from .register import Register


class StatusFlags(Enum):
    carry = 0x01  # Set if the add produced a carry, or if the subtraction produced a borrow.  Also holds bits after a logical shift.
    zero = 0x02  # Set if the result of the last operation (load/inc/dec/add/sub) was zero.
    interrupts_disabled = 0x04  # Set if maskable interrupts are disabled.
    decimal = 0x08  # Set if decimal mode active.(NES unused)
    breakpoint = 0x10  # Set if an interrupt caused by a BRK, reset if caused by an external interrupt.
    reserved = 0x20  # should always be 1
    overflow = 0x40  # Set if the addition of two like-signed numbers or the subtraction of two unlike-signed numbers produces a result greater than +127 or less than -128.
    sign = 0x80  # Set if bit 7 of the Accumulator is set


class StatusRegister(Register):
    def __init__(self, *args, **kwargs):
        super(StatusRegister, self).__init__(*args, **kwargs)
        self.flags = 0

    def __repr__(self):
        return "<StatusRegister {name}>".format(name=self.name)

    @property
    def carry(self):
        return self.flags & StatusFlags.carry.value

    @property
    def zero(self):
        return self.flags & StatusFlags.zero.value

    @property
    def interrupts_disabled(self):
        return self.flags & StatusFlags.interrupts_disabled.value

    @property
    def decimal(self):
        return self.flags & StatusFlags.decimal.value

    @property
    def breakpoint(self):
        return self.flags & StatusFlags.breakpoint.value

    @property
    def reserved(self):
        return self.flags & StatusFlags.reserved.value

    @property
    def overflow(self):
        return self.flags & StatusFlags.overflow.value

    @property
    def sign(self):
        return self.flags & StatusFlags.sign.value
