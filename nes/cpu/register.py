from ..memory import Memory


class Register(Memory):
    def __init__(self, name, description):
        super().__init__(1)
        self.name = name
        self.description = description
        self.contents = 0
