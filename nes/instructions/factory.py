from nes.addressing_modes import AddressingModeFactory
from .arithmetic import Adc, And, Asl


class InstructionFactory:
    classes = [
        Adc, And, Asl,
    ]

    @classmethod
    def create(cls, processor, info):
        addressing_mode = AddressingModeFactory.create(info['addressing_mode'])
        for instruction_class in cls.classes:
            if instruction_class.__name__.lower() == info['name'].lower():
                return instruction_class(processor, addressing_mode)
