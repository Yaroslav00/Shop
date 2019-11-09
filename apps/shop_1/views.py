from app import api,db
from models import *
from flask_restful import Resource, Api
from flask import jsonify
from flask import request

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class SignUp(Resource):
    def post(self):
        print(request.form)
        
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()
        jwt_token = User.encode_auth_token(user.id)
        print(jwt_token)
        return  jsonify(token=jwt_token, name=user.name)

class LogIn(Resource):
    def post(self):
        email = request.form.email
        password = request.form.password
        user = User.query.filter(email= email).one()
        if password == user.password:
            jwt_token = User.encode_auth_token(user.id)
        jwt_token = ""

        return  jsonify(token=jwt_token)


class IsAuth(Resource):
    def get(self):
        print(request.args)
      
        token = request.args.get('token')
        if token:
            try:
                user_id = User.decode_auth_token(token)
                print(user_id)
            except jwt.ExpiredSignatureError:
                return jsonify(message=-1)
            except jwt.InvalidSignatureError:
                return jsonify(message=-1)
            user = User.query.filter_by(id=user_id).first()
            return jsonify(message=0, name=user.name)
        return jsonify(message=-1)