class Bus:
    def __init__(self, name, description, width):
        self.name = name
        self.description = description
        self.width = width
        self.value = 0

    def put(self, value):
        self.value = value

    def get(self):
        return self.value
