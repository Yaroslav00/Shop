from app import db
import jwt
from config import SECRET_KEY
import datetime
class Good(db.Model):
    __tablename__ = "goods"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False,default=0)
    discount = db.Column(db.Integer, nullable=False,default=0)
    image_url = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Good %r>' % self.name

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String(50), nullable=False)
    def __init__(self,name,  email, password, admin=False):
        self.name= name
        self.email = email
        self.password = password
        self.admin = admin

    def encode_auth_token(user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=600),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    good_id =  db.Column(db.Integer, db.ForeignKey('goods.id'),
        nullable=False)
    good_quantity = db.Column(db.Integer, nullable=False, default=0)
    def __init__(self, user_id, good_id, good_quantity):
        self.user_id = user_id
        self.good_id = good_id
        self.good_quantity = good_quantity
    
class Interests(db.Model):
    __tablename__ = "interests"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    good_id =  db.Column(db.Integer, db.ForeignKey('goods.id'),
        nullable=False)
    def __init__(self, user_id, good_id):
        self.user_id = user_id
        self.good_id = good_id
    def __repr__(self):
        return "User_id: {0}".format(user_id)


