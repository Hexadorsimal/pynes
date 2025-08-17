from .register import Register


class ProcessorStatusRegister(Register):
    def __init__(self):
        self.n = False
        self.v = False
        self.x = False
        self.b = False
        self.d = False
        self.i = False
        self.z = False
        self.c = False

    def __repr__(self) -> str:
        return ''.join([
            letter if getattr(self, letter) else '-'
            for letter in 'nvxbdizc'
        ]).upper()

    @property
    def value(self) -> int:
        v = 0

        if self.n:
            v += 0x80

        if self.v:
            v += 0x40

        if self.x:
            v += 0x20

        if self.b:
            v += 0x10

        if self.d:
            v += 0x08

        if self.i:
            v += 0x04

        if self.z:
            v += 0x02

        if self.c:
            v += 0x01

        return v

    @value.setter
    def value(self, value) -> None:
        self.n = value & 0x80
        self.v = value & 0x40
        self.x = value & 0x20
        self.b = value & 0x10
        self.d = value & 0x08
        self.i = value & 0x04
        self.z = value & 0x02
        self.c = value & 0x01

    def update_negative_flag(self, value: int) -> None:
        if value & 0x80 != 0:
            self.n = True
        else:
            self.n = False

    def update_zero_flag(self, value: int) -> None:
        if value == 0:
            self.z = True
        else:
            self.z = False

    def update_overflow_flag(self, value: int) -> None:
        if value:
            self.v = True
        else:
            self.v = False

    def update_carry_flag(self, value: int) -> None:
        if value:
            self.c = True
        else:
            self.c = False
