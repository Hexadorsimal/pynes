from .register import Register


class GeneralPurposeRegister(Register):
    mask = 0xff

    def __init__(self, value: int = 0):
        self.value = value

    def read(self) -> int:
        return self.value

    def write(self, value: int) -> None:
        self.value = value

    def __eq__(self, other) -> bool:
        if isinstance(other, GeneralPurposeRegister):
            return self.value == other.value
        else:
            return self.value == other

    def __add__(self, other: int) -> int:
        return (self.value + other) & self.mask

    def __sub__(self, other: int) -> int:
        return (self.value - other) & self.mask

    def __iadd__(self, other: int) -> 'GeneralPurposeRegister':
        self.value += other
        self.value &= self.mask
        return self

    def __isub__(self, other: int) -> 'GeneralPurposeRegister':
        self.value -= other
        self.value &= self.mask
        return self
