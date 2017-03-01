from enum import Enum


class AddressMode(Enum):
    immediate = "imm"
    absolute = "abs"
    zero_page = "zpg"
    implied = "imp"
    indirect_absolute = "iab"
    absolute_indexed_x = "aix"
    absolute_indexed_y = "aiy"
    zeroPage_indexed_x = "zpx"
    zeroPage_indexed_y = "zpy"
    indexed_indirect_x = "iix"
    indirect_indexed_y = "iiy"
    relative = "rel"
    accumulator = "acc"
