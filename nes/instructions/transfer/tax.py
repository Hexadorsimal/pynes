from .transfer import TransferInstruction


class Tax(TransferInstruction):
    src = 'a'
    dst = 'x'
    update_flags = True
