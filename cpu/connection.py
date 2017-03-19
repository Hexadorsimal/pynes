class Connection:
    def __init__(self, name, enabled=False):
        self.name = name
        self.enabled = enabled

    def __repr__(self):
        return f"{self.name}"
