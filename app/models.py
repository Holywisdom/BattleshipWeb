from app import app
from app import db
import re

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
   # board = db.relationship('Board', backref = 'player', lazy = 'dynamic')

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self): # pragma: no cover
        return '<User %r>' % (self.nickname)

    @staticmethod
    def make_valid_nickname(nickname):
        return re.sub('[^a-zA-Z0-9_\.]', '', nickname)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname = nickname).first() == None:
            return nickname
        version =2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname = new_nickname).first() == None:
                    break
            version += 1
        return new_nickname

#class Board(Model):
#    id = db.Column(db.Integer, primary_key = True)
#    board = db.Column(db.String(300))
#    timestamp = db.Column(db.DateTime)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#    def __repr__(self): # pragma: no cover
#        return '<Post %r>' % (self.body)
