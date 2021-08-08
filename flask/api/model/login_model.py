from api import db
import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(32))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<User %r>' % self.name