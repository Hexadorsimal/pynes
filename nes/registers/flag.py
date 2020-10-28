class Flag:
    def __init__(self, value=False, mask=None):
        self.value = value
        self.mask = mask

    def __bool__(self):
        return self.value

    def set(self):
        self.value = True

    def clear(self):
        self.value = False
