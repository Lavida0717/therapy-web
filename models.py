from . import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"Booking('{self.name}', '{self.email}', '{self.date}')"
