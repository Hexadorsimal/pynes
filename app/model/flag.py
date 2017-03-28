from .. import db


class Flag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    letter = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    mask = db.Column(db.Integer)
    register_id = db.Column(db.Integer, db.ForeignKey("register.id"))

    register = db.relationship("Register", backref=db.backref("flags"))

    def __init__(self, letter, name, description, mask, register_id):
        self.letter = letter
        self.name = name
        self.description = description
        self.mask = mask
        self.register_id = register_id
