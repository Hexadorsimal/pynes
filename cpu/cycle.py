class Cycle:
    def __init__(self, operations=[]):
        self.operations = operations

    def add_operation(self, operation):
        self.operations.append(operation)

    def execute(self):
        for operation in self.operations:
            operation.execute()
