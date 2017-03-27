from .. import db


class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    addressing_mode_id = db.Column(db.Integer, db.ForeignKey("addressing_mode.id"))

    addressing_mode = db.relationship("AddressingMode", backref=db.backref("instructions"))

    def __init__(self, id, addressing_mode_id, name, description):
        self.id = id
        self.addressing_mode_id = addressing_mode_id
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Instruction {name}>'.format(name=self.name)
