class Cycle:
    def __init__(self, microinstructions):
        self.microinstructions = microinstructions

    def __repr__(self):
        return str(self.microinstructions)

    def add_microinstruction(self, microinstruction):
        self.microinstructions.append(microinstruction)

    def execute(self, cpu):
        for microinstruction in self.microinstructions:
            microinstruction.execute(cpu)
