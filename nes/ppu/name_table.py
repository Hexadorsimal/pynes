class NameTable:
    width = 256
    height = 240

    def __init__(self, data=None):
        self.data = data
        if not self.data:
            self.data = bytearray(1024)
