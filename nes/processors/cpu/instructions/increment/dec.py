from .increment_memory import IncrementMemoryInstruction


class Dec(IncrementMemoryInstruction):
    amount = -1
