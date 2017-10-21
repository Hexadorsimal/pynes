from .bcc import Bcc
from .bcs import Bcs
from .beq import Beq
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
from .dex import Dex
from .dey import Dey
from .inx import Inx
from .iny import Iny
from .jmp import JmpAbsolute, JmpIndirectAbsolute
from .lda import LdaAbsolute, LdaAbsoluteX, LdaAbsoluteY, LdaImmediate, LdaIndexedIndirect, LdaIndirectIndexed, LdaZeroPage, LdaZeroPageX
from .ldx import LdxAbsolute, LdxAbsoluteY, LdxImmediate, LdxZeroPage, LdxZeroPageY
from .ldy import LdyAbsolute, LdyAbsoluteX, LdyImmediate, LdyZeroPage, LdyZeroPageX
from .nop import Nop
from .pha import Pha
from .php import Php
from .pla import Pla
from .plp import Plp
from .rti import Rti
from .rts import Rts
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
    Bcc,
    Bcs,
    Beq,
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
    Dex,
    Dey,
    Inx,
    Iny,
    JmpAbsolute, JmpIndirectAbsolute,
    LdaAbsolute, LdaAbsoluteX, LdaAbsoluteY, LdaImmediate, LdaIndexedIndirect, LdaIndirectIndexed, LdaZeroPage, LdaZeroPageX,
    LdxAbsolute, LdxAbsoluteY, LdxImmediate, LdxZeroPage, LdxZeroPageY,
    LdyAbsolute, LdyAbsoluteX, LdyImmediate, LdyZeroPage, LdyZeroPageX,
    Nop,
    Pha,
    Php,
    Pla,
    Plp,
    Rti,
    Rts,
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
