from datetime import datetime
from db import db


class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text(), nullable=False)

    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Posts %r>' % self.id

    