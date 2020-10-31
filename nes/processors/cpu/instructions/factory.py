from .addressing_modes import AddressingModeFactory
from .arithmetic import Adc, And, Asl, Eor, Lsr, Ora, Rol, Ror, Sbc
from .branch import Bcc, Bcs, Beq, Bmi, Bne, Bpl, Bvc, Bvs
from .compare import Bit, Cmp, Cpx, Cpy
from .flags import Sec, Sed, Sei, Clc, Cld, Cli, Clv
from .inc_dec import Inc, Inx, Iny, Dec, Dex, Dey
from .interrupt import Brk, Rti
from .jump import Jmp
from .load_store import Lda, Ldx, Ldy, Sta, Stx, Sty
from .nop import Nop
from .stack import Pha, Php, Pla, Plp
from .subroutine import Jsr, Rts
from .transfer import Tax, Tay, Tsx, Txa, Txs, Tya


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

    @classmethod
    def create(cls, processor, info):
        addressing_mode = AddressingModeFactory.create(info['addressing_mode'])

        parameter = addressing_mode.read_parameter(processor)

        for instruction_class in cls.classes:
            if instruction_class.__name__.lower() == info['name'].lower():
                return instruction_class(addressing_mode, info['size'], info['cycles'], info['page_cycles'], parameter)
