from .general_purpose_register import GeneralPurposeRegister


class StackPointer(GeneralPurposeRegister):
    def __init__(self, value=0):
        super().__init__(value)

    @property
    def hi(self):
        return 0x01

    @property
    def pointer(self):
        return (self.hi << 8) | self.lo
