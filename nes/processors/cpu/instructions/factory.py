from . import AddressingMode, Instruction
from .addressing_modes import AddressingModeFactory
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
from .. import Cpu


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
    def create(cls, cpu: Cpu, name: str, addressing_mode: AddressingMode, cycles=0, page_cycles=0, parameter=None) -> Instruction | None:
        addressing_mode = AddressingModeFactory.create(addressing_mode)

        if not parameter:
            parameter = cls.read_parameter(cpu, addressing_mode.parameter_size)

        if name.lower() in cls.class_map:
            return cls.class_map[name.lower()](addressing_mode, cycles, page_cycles, parameter)
        else:
            return None

    @staticmethod
    def read_parameter(cpu: Cpu, parameter_size: int) -> int:
        lo = 0
        hi = 0

        if parameter_size > 0:
            lo = cpu.read(cpu.pc + 1)

        if parameter_size > 1:
            hi = cpu.read(cpu.pc + 2)

        return (hi << 8) | lo
