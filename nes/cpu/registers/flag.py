class Flag:
    def __init__(self, letter, name, description, mask):
        self.letter = letter
        self.name = name
        self.mask = mask
        self.description = description

    def __repr__(self):
        return '{letter}: {mask}'.format(letter=self.letter, mask=hex(self.mask))
