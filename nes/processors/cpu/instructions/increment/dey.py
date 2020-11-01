from .increment_register import IncrementRegisterInstruction


class Dey(IncrementRegisterInstruction):
    register_name = 'y'
    amount = -1
