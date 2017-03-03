class Line:
    def __init__(self, name, description, enabled=False):
        self.name = name
        self.description = description
        self.enabled = enabled

    def __repr__(self):
        return f"{self.name}: {self.description}"
