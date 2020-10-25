class Flag:
    def __init__(self, value=0):
        self.value = value

    def get(self):
        return self.value

    def set(self):
        self.value = 1

    def clear(self):
        self.value = 0

    def update(self, value):
        pass
