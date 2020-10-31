from .transfer import TransferInstruction


class Txa(TransferInstruction):
    src = 'x'
    dst = 'a'
    update_flags = True
