from .absolute import AbsoluteParameterReader
from .absolute_x import AbsoluteXParameterReader
from .absolute_y import AbsoluteYParameterReader
from .immediate import ImmediateParameterReader
from .indexed_indirect import IndexedIndirectParameterReader
from .indirect import IndirectParameterReader
from .indirect_indexed import IndirectIndexedParameterReader
from .parameter_reader import ParameterReader
from .relative import RelativeParameterReader
from .result_writer import ResultWriter
from .zero_page import ZeroPageParameterReader
from .zero_page_x import ZeroPageXParameterReader
from .zero_page_y import ZeroPageYParameterReader


def get_parameter_reader(addressing_mode: str) -> ParameterReader | None:
    readers = {
        'Absolute': AbsoluteParameterReader,
        'AbsoluteX': AbsoluteXParameterReader,
        'AbsoluteY': AbsoluteYParameterReader,
        'Immediate': ImmediateParameterReader,
        'IndexedIndirect': IndexedIndirectParameterReader,
        'Indirect': IndirectParameterReader,
        'IndirectIndexed': IndirectIndexedParameterReader,
        'Relative': RelativeParameterReader,
        'ZeroPage': ZeroPageParameterReader,
        'ZeroPageX': ZeroPageXParameterReader,
        'ZeroPageY': ZeroPageYParameterReader,
    }

    return readers.get(addressing_mode)

def get_result_writer(addressing_mode: str) -> ResultWriter | None:
    writers = {}

    return writers.get(addressing_mode)
