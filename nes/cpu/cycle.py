class Cycle:
    def __init__(self, microinstructions=[]):
        self.microinstructions = microinstructions

    def add_microinstruction(self, microinstruction):
        self.microinstructions.append(microinstruction)

    def execute(self):
        for microinstruction in self.microinstructions:
            microinstruction.execute()
