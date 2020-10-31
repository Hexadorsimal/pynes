from .transfer import TransferInstruction


class Txs(TransferInstruction):
    src = 'x'
    dst = 's'
    update_flags = False
