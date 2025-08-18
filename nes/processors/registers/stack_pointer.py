from .general_purpose_register import GeneralPurposeRegister


class StackPointer(GeneralPurposeRegister):
    def read_address(self) -> int:
        return 0x0100 | self.read()
