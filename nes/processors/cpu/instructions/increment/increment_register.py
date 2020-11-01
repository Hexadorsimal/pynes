from .increment import IncrementInstruction


class IncrementRegisterInstruction(IncrementInstruction):
    register_name = None

    def increment(self, processor):
        register = processor.registers[self.register_name]
        register.value += self.amount
        return register.value
