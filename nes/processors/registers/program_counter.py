from .general_purpose_register import GeneralPurposeRegister


class ProgramCounter:
    def __init__(self):
        self.hi = GeneralPurposeRegister()
        self.lo = GeneralPurposeRegister()

    def read_address(self) -> int:
        return (self.hi.read() << 8) | self.lo.read()
