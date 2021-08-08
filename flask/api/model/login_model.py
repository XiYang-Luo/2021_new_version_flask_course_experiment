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

class BlastModel(db.Model):
    __tablename__ = 'blast'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(255),index=True)
    project_name = db.Column(db.String(255))
    db_ncbi = db.Column(db.String(255))
    sequence = db.Column(db.Text(16777216))
    e_value = db.Column(db.String(255), default='0.04')
    content_seq = db.Column(db.String(255))
    content_e_value = db.Column(db.String(255))
    content_lenght = db.Column(db.String(255))
    content_hsp_match = db.Column(db.Text(16777216))
    content_hsp_query = db.Column(db.Text(16777216))
    content_hsp_sbjct = db.Column(db.Text(16777216))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<Blast %r>' % self.project_name