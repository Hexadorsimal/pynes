from .general_purpose_register import GeneralPurposeRegister


class ProgramCounter(GeneralPurposeRegister):
    bits = 16
    mask = 0xffff

    @property
    def hi(self):
        return (self._value >> 8) & 0xff

