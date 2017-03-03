class Register:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Register {name}>".format(name=self.name)

    @property
    def value(self):
        raise NotImplementedError
