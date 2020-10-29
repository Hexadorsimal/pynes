from nes.addressing_modes import AddressingModeFactory
from .arithmetic import Adc, And, Asl, Bit, Cmp, Cpx, Cpy, Eor, Lsr, Nop, Ora, Rol, Ror, Sbc
from .branch import Bcc, Bcs, Beq, Bmi, Bne, Bpl, Brk, Bvc, Bvs, Jmp, Jsr, Rti, Rts
from .clear import Clc, Cld, Cli, Clv
from .decrement import Dec, Dex, Dey
from .increment import Inc, Inx, Iny
from .load import Lda, Ldx, Ldy
from .set import Sec, Sed, Sei
from .stack import Pha, Php, Pla, Plp
from .store import Sta, Stx, Sty
from .transfer import Tax, Tay, Tsx, Txa, Txs, Tya


class InstructionFactory:
    classes = [
        Adc, And, Asl, Bit, Cmp, Cpx, Cpy, Eor, Lsr, Nop, Ora, Rol, Ror, Sbc,
        Bcc, Bcs, Beq, Bmi, Bne, Bpl, Brk, Bvc, Bvs, Jmp, Jsr, Rti, Rts,
        Clc, Cld, Cli, Clv,
        Dec, Dex, Dey,
        Inc, Inx, Iny,
        Lda, Ldx, Ldy,
        Sec, Sed, Sei,
        Pha, Php, Pla, Plp,
        Sta, Stx, Sty,
        Tax, Tay, Tsx, Txa, Txs, Tya,
    ]

    @classmethod
    def create(cls, processor, info):
        addressing_mode = AddressingModeFactory.create(info['addressing_mode'])

        param = addressing_mode.read_parameter(processor)

        for instruction_class in cls.classes:
            if instruction_class.__name__.lower() == info['name'].lower():
                return instruction_class(addressing_mode, info['size'], info['cycles'], info['page_cycles'], param)
