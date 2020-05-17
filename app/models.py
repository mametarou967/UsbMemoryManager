from datetime import datetime
from app import login
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User id:{0} username{1}>'.format(self.id,self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UsbMemory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usb_number = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<UsbMemory id:{0} usb_number:{1} user_id:{2}>'.format(self.id,self.usb_number,self.user_id)

class Rireki(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    usbMemory_id = db.Column(db.Integer, db.ForeignKey('usbMemory.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    rireki_id = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Rireki id:{0} loan_id:{1} timestamp:{2} rireki_id:{3}>'.format(self.id,self.loan_id,self.timestamp,self.rireki_id)

