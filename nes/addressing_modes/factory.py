from .absolute import AbsoluteAddressingMode
from .absolute_x import AbsoluteXAddressingMode
from .absolute_y import AbsoluteYAddressingMode
from .accumulator import AccumulatorAddressingMode
from .immediate import ImmediateAddressingMode
from .implied import ImpliedAddressingMode
from .indexed_indirect import IndexedIndirectAddressingMode
from .indirect import IndirectAddressingMode
from .indirect_indexed import IndirectIndexedAddressingMode
from .relative import RelativeAddressingMode
from .zero_page import ZeroPageAddressingMode
from .zero_page_x import ZeroPageXAddressingMode
from .zero_page_y import ZeroPageYAddressingMode


class AddressingModeFactory:
    classes = [
        AbsoluteAddressingMode,
        AbsoluteXAddressingMode,
        AbsoluteYAddressingMode,
        AccumulatorAddressingMode,
        ImmediateAddressingMode,
        ImpliedAddressingMode,
        IndexedIndirectAddressingMode,
        IndirectAddressingMode,
        IndirectIndexedAddressingMode,
        RelativeAddressingMode,
        ZeroPageAddressingMode,
        ZeroPageXAddressingMode,
        ZeroPageYAddressingMode,
    ]

    @classmethod
    def create(cls, name):
        for addressing_mode_class in cls.classes:
            if addressing_mode_class.__name__.replace('AddressingMode', '').lower() == name.lower():
                return addressing_mode_class()
