from . import Instruction
from .arithmetic import Adc, And, Asl, Eor, Lsr, Ora, Rol, Ror, Sbc
from .branch import Bcc, Bcs, Beq, Bmi, Bne, Bpl, Bvc, Bvs
from .compare import Bit, Cmp, Cpx, Cpy
from .flags import Sec, Sed, Sei, Clc, Cld, Cli, Clv
from .increment import Inc, Inx, Iny, Dec, Dex, Dey
from .interrupt import Brk, Rti
from .jump import Jmp
from .load_store import Lda, Ldx, Ldy, Sta, Stx, Sty
from .nop import Nop
from .stack import Pha, Php, Pla, Plp
from .subroutine import Jsr, Rts
from .transfer import Tax, Tay, Tsx, Txa, Txs, Tya
from ..addressing_modes import get_parameter_reader, get_result_writer
from ..decoder import Opcode


class InstructionFactory:
    classes = [
        Adc, And, Asl, Eor, Lsr, Ora, Rol, Ror, Sbc,
        Bcc, Bcs, Beq, Bmi, Bne, Bpl, Bvc, Bvs,
        Bit, Cmp, Cpx, Cpy, Nop,
        Inc, Inx, Iny, Dec, Dex, Dey,
        Brk, Jmp, Jsr, Rti, Rts,
        Lda, Ldx, Ldy, Sta, Stx, Sty,
        Sec, Sed, Sei, Clc, Cld, Cli, Clv,
        Pha, Php, Pla, Plp,
        Tax, Tay, Tsx, Txa, Txs, Tya,
    ]

    class_map = {}

    for cls in classes:
        class_map[cls.__name__.lower()] = cls

    @classmethod
    def create(cls, opcode: Opcode, params: list[int]) -> Instruction | None:
        if opcode.name.lower() in cls.class_map:
            reader = get_parameter_reader(opcode.addressing_mode)
            writer = get_result_writer(opcode.addressing_mode)
            return cls.class_map[opcode.name.lower()](opcode, params, reader, writer)
        else:
            return None
