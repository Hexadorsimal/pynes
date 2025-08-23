from .transfer import TransferInstruction


class Tya(TransferInstruction):
    src = 'y'
    dst = 'a'
    update_flags = True
