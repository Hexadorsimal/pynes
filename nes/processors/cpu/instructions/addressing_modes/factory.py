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
    classes = {
        'absolute': AbsoluteAddressingMode,
        'absolutex': AbsoluteXAddressingMode,
        'absolutey': AbsoluteYAddressingMode,
        'accumulator': AccumulatorAddressingMode,
        'immediate': ImmediateAddressingMode,
        'implied': ImpliedAddressingMode,
        'indexedindirect': IndexedIndirectAddressingMode,
        'indirect': IndirectAddressingMode,
        'indirectindexed': IndirectIndexedAddressingMode,
        'relative': RelativeAddressingMode,
        'zeropage': ZeroPageAddressingMode,
        'zeropagex': ZeroPageXAddressingMode,
        'zeropagey': ZeroPageYAddressingMode,
    }

    @classmethod
    def create(cls, name):
        if name.lower() in cls.classes:
            return cls.classes[name.lower()]()
