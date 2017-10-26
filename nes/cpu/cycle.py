class Cycle:
    def __init__(self, microinstructions, read_write='read'):
        self.read_write = read_write
        self.microinstructions = microinstructions

    def __repr__(self):
        return str(self.microinstructions) + ' ' + self.read_write

    def add_microinstruction(self, microinstruction):
        self.microinstructions.append(microinstruction)

    def execute(self, cpu):
        for microinstruction in self.microinstructions:
            microinstruction.execute(cpu)
