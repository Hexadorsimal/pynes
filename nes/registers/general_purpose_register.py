from .register import Register


class GeneralPurposeRegister(Register):
    bits = 8
    mask = 0xff

    def __init__(self, value=0):
        self._value = value

    def __repr__(self):
        return f'{self._value:#X}'

    @property
    def hi(self):
        raise IndexError('This register does not have an upper byte')

    @property
    def lo(self):
        return self._value & 0xff

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __add__(self, other):
        return (self._value + other) & self.mask

    def __sub__(self, other):
        return (self._value - other) & self.mask

    def __iadd__(self, other):
        self._value += other
        self._value &= self.mask
        return self

    def __isub__(self, other):
        self._value -= other
        self._value &= self.mask
        return self
