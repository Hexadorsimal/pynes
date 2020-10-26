class Flag:
    def __init__(self, value=0):
        self.value = value

    def __bool__(self):
        return self.value != 0

    def set(self):
        self.value = 1

    def clear(self):
        self.value = 0
