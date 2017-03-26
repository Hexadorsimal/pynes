from .. import db


class Instruction(db.Model):
    opcode = db.Column(db.Integer, primary_key=True)
    addressing_mode = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)

    def __init__(self, opcode, addressing_mode, name, description):
        self.opcode = opcode
        self.addressing_mode = addressing_mode
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Instruction {name}>'.format(name=self.name)
