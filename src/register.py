class Register:
    def __init__(self, name, description, bit_count):
        self.name = name
        self.description = description
        self.bit_count = bit_count

    def __repr__(self):
        return "<Register {name}>".format(name=self.name)
