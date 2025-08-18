from .addressing_mode import AddressingMode
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


addressing_modes = {
    'absolute': AbsoluteAddressingMode(),
    'absolutex': AbsoluteXAddressingMode(),
    'absolutey': AbsoluteYAddressingMode(),
    'accumulator': AccumulatorAddressingMode(),
    'immediate': ImmediateAddressingMode(),
    'implied': ImpliedAddressingMode(),
    'indexedindirect': IndexedIndirectAddressingMode(),
    'indirect': IndirectAddressingMode(),
    'indirectindexed': IndirectIndexedAddressingMode(),
    'relative': RelativeAddressingMode(),
    'zeropage': ZeroPageAddressingMode(),
    'zeropagex': ZeroPageXAddressingMode(),
    'zeropagey': ZeroPageYAddressingMode(),
}


def get_addressing_mode(name: str) -> AddressingMode:
    if name.lower() in addressing_modes:
        return addressing_modes[name.lower()]

    raise ValueError(name)
