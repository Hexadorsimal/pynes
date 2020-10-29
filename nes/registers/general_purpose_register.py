from .register import Register


class GeneralPurposeRegister(Register):
    def __init__(self, value=0, mask=0xff):
        self._value = value
        self.mask = mask

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
