from core import db
from datetime import datetime

class Wel(db.Model):
    __tablename__ = 'wels'
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer(),nullable=False)
    distance = db.Column(db.Integer(),nullable=False)

    def __repr__(self) -> str:
        return self.title     