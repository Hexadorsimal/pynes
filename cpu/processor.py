class Processor:
    def __init__(self, registers):
        self.registers = {}
        for register in registers:
            self.registers[register.name] = register

        self.cycle_queue = []

    def step(self):
        if self.cycle_queue:
            cycle = self.cycle_queue.pop(0)
            for operation in cycle:
                operation.execute()
