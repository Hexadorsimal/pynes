from nes.memory import Memory


class Register(Memory):
    def __init__(self, name, description):
        super().__init__(1)
        self.name = name
        self.description = description
        self.contents = 0

    def __repr__(self):
        return hex(self.contents)

    def read(self, addr):
        if addr != 0:
            raise IndexError
        return self.contents

    def write(self, addr, data):
        if addr != 0:
            raise IndexError
        self.contents = data

    def copy(self, src):
        self.contents = src.contents