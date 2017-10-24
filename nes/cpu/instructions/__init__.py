from .adc import AdcAbsolute, AdcAbsoluteX, AdcAbsoluteY, AdcImmediate, AdcIndexedIndirect, AdcIndirectIndexed, AdcZeroPage, AdcZeroPageX
from .and_ import AndAbsolute, AndAbsoluteX, AndAbsoluteY, AndImmediate, AndIndexedIndirect, AndIndirectIndexed, AndZeroPage, AndZeroPageX
from .asl import AslAbsolute, AslAbsoluteX, AslAccumulator, AslZeroPage, AslZeroPageX
from .bcc import Bcc
from .bcs import Bcs
from .beq import Beq
from .bit import BitAbsolute, BitZeroPage
from .bmi import Bmi
from .bne import Bne
from .bpl import Bpl
from .brk import Brk
from .bvc import Bvc
from .bvs import Bvs
from .clc import Clc
from .cld import Cld
from .cli import Cli
from .clv import Clv
from .cmp import CmpAbsolute, CmpAbsoluteX, CmpAbsoluteY, CmpImmediate, CmpIndexedIndirect, CmpIndirectIndexed, CmpZeroPage, CmpZeroPageX
from .cpx import CpxAbsolute, CpxImmediate, CpxZeroPage
from .cpy import CpyAbsolute, CpyImmediate, CpyZeroPage
from .dec import DecAbsolute, DecAbsoluteX, DecZeroPage, DecZeroPageX
from .dex import Dex
from .dey import Dey
from .eor import EorAbsolute, EorAbsoluteX, EorAbsoluteY, EorImmediate, EorIndexedIndirect, EorIndirectIndexed, EorZeroPage, EorZeroPageX
from .inc import IncAbsolute, IncAbsoluteX, IncZeroPage, IncZeroPageX
from .inx import Inx
from .iny import Iny
from .jmp import JmpAbsolute, JmpIndirectAbsolute
from .jsr import Jsr
from .lda import LdaAbsolute, LdaAbsoluteX, LdaAbsoluteY, LdaImmediate, LdaIndexedIndirect, LdaIndirectIndexed, LdaZeroPage, LdaZeroPageX
from .ldx import LdxAbsolute, LdxAbsoluteY, LdxImmediate, LdxZeroPage, LdxZeroPageY
from .ldy import LdyAbsolute, LdyAbsoluteX, LdyImmediate, LdyZeroPage, LdyZeroPageX
from .lsr import LsrAbsolute, LsrAbsoluteX, LsrAccumulator, LsrZeroPage, LsrZeroPageX
from .nop import Nop
from .ora import OraAbsolute, OraAbsoluteX, OraAbsoluteY, OraImmediate, OraIndexedIndirect, OraIndirectIndexed, OraZeroPage, OraZeroPageX
from .pha import Pha
from .php import Php
from .pla import Pla
from .plp import Plp
from .rol import RolAbsolute, RolAbsoluteX, RolAccumulator, RolZeroPage, RolZeroPageX
from .ror import RorAbsolute, RorAbsoluteX, RorAccumulator, RorZeroPage, RorZeroPageX
from .rti import Rti
from .rts import Rts
from .sbc import SbcAbsolute, SbcAbsoluteX, SbcAbsoluteY, SbcImmediate, SbcIndexedIndirect, SbcIndirectIndexed, SbcZeroPage, SbcZeroPageX
from .sec import Sec
from .sed import Sed
from .sei import Sei
from .sta import StaAbsolute, StaAbsoluteX, StaAbsoluteY, StaIndexedIndirect, StaIndirectIndexed, StaZeroPage, StaZeroPageX
from .stx import StxAbsolute, StxZeroPage, StxZeroPageY
from .sty import StyAbsolute, StyZeroPage, StyZeroPageX
from .tax import Tax
from .tay import Tay
from .tsx import Tsx
from .txa import Txa
from .txs import Txs
from .tya import Tya

all_instructions = [
    AdcAbsolute, AdcAbsoluteX, AdcAbsoluteY, AdcImmediate, AdcIndexedIndirect, AdcIndirectIndexed, AdcZeroPage, AdcZeroPageX,
    AndAbsolute, AndAbsoluteX, AndAbsoluteY, AndImmediate, AndIndexedIndirect, AndIndirectIndexed, AndZeroPage, AndZeroPageX,
    AslAbsolute, AslAbsoluteX, AslAccumulator, AslZeroPage, AslZeroPageX,
    Bcc,
    Bcs,
    Beq,
    BitAbsolute, BitZeroPage,
    Bmi,
    Bne,
    Bpl,
    Brk,
    Bvc,
    Bvs,
    Clc,
    Cld,
    Cli,
    Clv,
    CmpAbsolute, CmpAbsoluteX, CmpAbsoluteY, CmpImmediate, CmpIndexedIndirect, CmpIndirectIndexed, CmpZeroPage, CmpZeroPageX,
    CpxAbsolute, CpxImmediate, CpxZeroPage,
    CpyAbsolute, CpyImmediate, CpyZeroPage,
    DecAbsolute, DecAbsoluteX, DecZeroPage, DecZeroPageX,
    Dex,
    Dey,
    EorAbsolute, EorAbsoluteX, EorAbsoluteY, EorImmediate, EorIndexedIndirect, EorIndirectIndexed, EorZeroPage, EorZeroPageX,
    IncAbsolute, IncAbsoluteX, IncZeroPage, IncZeroPageX,
    Inx,
    Iny,
    JmpAbsolute, JmpIndirectAbsolute,
    Jsr,
    LdaAbsolute, LdaAbsoluteX, LdaAbsoluteY, LdaImmediate, LdaIndexedIndirect, LdaIndirectIndexed, LdaZeroPage, LdaZeroPageX,
    LdxAbsolute, LdxAbsoluteY, LdxImmediate, LdxZeroPage, LdxZeroPageY,
    LdyAbsolute, LdyAbsoluteX, LdyImmediate, LdyZeroPage, LdyZeroPageX,
    LsrAbsolute, LsrAbsoluteX, LsrAccumulator, LsrZeroPage, LsrZeroPageX,
    Nop,
    OraAbsolute, OraAbsoluteX, OraAbsoluteY, OraImmediate, OraIndexedIndirect, OraIndirectIndexed, OraZeroPage, OraZeroPageX,
    Pha,
    Php,
    Pla,
    Plp,
    RolAbsolute, RolAbsoluteX, RolAccumulator, RolZeroPage, RolZeroPageX,
    RorAbsolute, RorAbsoluteX, RorAccumulator, RorZeroPage, RorZeroPageX,
    Rti,
    Rts,
    SbcAbsolute, SbcAbsoluteX, SbcAbsoluteY, SbcImmediate, SbcIndexedIndirect, SbcIndirectIndexed, SbcZeroPage, SbcZeroPageX,
    Sec,
    Sed,
    Sei,
    StaAbsolute, StaAbsoluteX, StaAbsoluteY, StaIndexedIndirect, StaIndirectIndexed, StaZeroPage, StaZeroPageX,
    StxAbsolute, StxZeroPage, StxZeroPageY,
    StyAbsolute, StyZeroPage, StyZeroPageX,
    Tax,
    Tay,
    Tsx,
    Txa,
    Txs,
    Tya,
]
