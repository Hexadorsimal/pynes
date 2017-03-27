from .. import db


class OpCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instruction_id = db.Column(db.Integer, db.ForeignKey("instruction.id"))
    addressing_mode_id = db.Column(db.Integer, db.ForeignKey("addressing_mode.id"))

    instruction = db.relationship("Instruction", backref=db.backref("opcodes"))
    addressing_mode = db.relationship("AddressingMode", backref=db.backref("opcodes"))

    def __init__(self, id, instruction_id, addressing_mode_id):
        self.id = id
        self.instruction_id = instruction_id
        self.addressing_mode_id = addressing_mode_id
