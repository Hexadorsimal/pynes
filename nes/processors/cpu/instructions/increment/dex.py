from .increment_register import IncrementRegisterInstruction


class Dex(IncrementRegisterInstruction):
    register_name = 'x'
    amount = -1
