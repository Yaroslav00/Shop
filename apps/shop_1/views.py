from app import api,db,mail
from models import *
from flask_restful import Resource, Api
from flask import jsonify
from flask import request
import jwt


class SignUp(Resource):
    def post(self):        
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()
        jwt_token = User.encode_auth_token(user.id)
        print(jwt_token)
        return  jsonify(token=jwt_token, name=user.name)


class LogIn(Resource):
    def post(self):
        print(request.form)
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email= email).first()
        jwt_token = ""
        if password == user.password:
            jwt_token = User.encode_auth_token(user.id)
        
        return  jsonify(token=jwt_token, name=user.name, admin=user.admin)


class Mails(Resource):
    def get(self):
        mail.send_message(
            'Send Mail tutorial!',
            sender='yarik.voytovich@gmail.com',
            recipients=['voytovichyaroslav1@gmail.com'],
            body="Congratulations you've succeeded!"
        )
        return 'Mail sent'
