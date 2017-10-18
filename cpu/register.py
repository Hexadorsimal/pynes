class Register:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self._contents = 0

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        self._contents = value
