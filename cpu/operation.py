from enum import Enum, auto


class OperationType(Enum):
    set = auto()
    clear = auto()
    move = auto()
    alu = auto()


class AluFunction(Enum):
    increment = auto()
    decrement = auto()
    add = auto()
    subtract = auto()
    multiply = auto()
    divide = auto()
    compare = auto()
    and_ = auto()
    or_ = auto()
    xor = auto()
    arithmetic_shift_left = auto()
    arithmetic_shift_right = auto()
    logical_shift_left = auto()
    logical_shift_right = auto()
    rotate_left = auto()
    rotate_right = auto()


class Operation:
    def execute(self, processor):
        raise NotImplementedError


class SetFlagOperation(Operation):
    def __init__(self, flag):
        self.flag = flag

    def execute(self, processor):
        flag_register = processor.registers['P']
        flag_register.set_flag(self.flag)


class ClearFlagOperation(Operation):
    def __init__(self, flag):
        self.flag = flag

    def execute(self, processor):
        flag_register = processor.registers['P']
        flag_register.clear_flag(self.flag)


class MoveOperation(Operation):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def execute(self, processor):
        src_register = processor.registers[self.src]
        dst_register = processor.registers[self.dst]
        dst_register.value = src_register.value


class AluOperation(Operation):
    def __init__(self, input_a, input_b, alu_functionn, dst_register):
        self.input_a = input_a
        self.input_b = input_b
        self.alu_function = alu_functionn
        self.dst_register = dst_register

    def execute(self, processor):
        pass
