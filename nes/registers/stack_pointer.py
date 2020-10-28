from .general_purpose_register import GeneralPurposeRegister


class StackPointer(GeneralPurposeRegister):
    def __init__(self, value=0, mask=0xff, page=0x0100):
        super().__init__(value, mask)
        self.page = page

    @property
    def addr(self):
        return self.page | self.value
