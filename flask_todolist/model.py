#model.py

from app import db
import datetime


class List(db.Model):
    __table__name = 'list'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
    updata_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    deleted_at = db.Column(db.TIMESTAMP)

    def __init__(self, content):
        self.content = content

    def to_json(self):
        return {
            "id": self.id,
            "content": self.content,
            "created_at": self.created_at,
        }