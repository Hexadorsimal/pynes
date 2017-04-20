from .. import db


class OpCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instruction_id = db.Column(db.Integer, db.ForeignKey("instruction.id"))
    addressing_mode_id = db.Column(db.Integer, db.ForeignKey("addressing_mode.id"))

    instruction = db.relationship("Instruction", backref=db.backref("opcodes"))
    addressing_mode = db.relationship("AddressingMode", backref=db.backref("opcodes"))

    @property
    def name(self):
        return hex(self.id)[2:].upper()
