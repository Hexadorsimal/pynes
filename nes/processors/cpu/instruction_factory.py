from typing import Callable

from .instruction import Instruction
from .decoder import Opcode
from .parameter_reader import ParameterReader
from .result_writer import ResultWriter


class InstructionFactory:
    def __init__(self,
        classes: list[type],
        get_parameter_reader: Callable[[str], ParameterReader],
        get_result_writer: Callable[[str], ResultWriter],
    ):
        self.class_map = {}

        for cls in classes:
            self.class_map[cls.__name__.lower()] = cls

        self.get_parameter_reader = get_parameter_reader
        self.get_result_writer = get_result_writer

    def create(self, opcode: Opcode, params: list[int]) -> Instruction | None:
        if opcode.name.lower() in self.class_map:
            reader = self.get_parameter_reader(opcode.addressing_mode)
            writer = self.get_result_writer(opcode.addressing_mode)
            return self.class_map[opcode.name.lower()](opcode, params, reader, writer)
        else:
            return None
