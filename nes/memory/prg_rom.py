from .rom import Rom


class PrgRom(Rom):
    page_size = 16 * 1024

    def __init__(self, data):
        super().__init__(self.page_size, data)
