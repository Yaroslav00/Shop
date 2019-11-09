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
        email = request.email
        password = request.password
        user = User.query.filter(email= email).one()
        if password == user.password:
            jwt_token = User.encode_auth_token(user.id)
        jwt_token = ""

        return  jsonify(token=jwt_token)


class IsAuth(Resource):
    def get(self):
        print(request.args)
        print(request.params)
        token = request.args.get('token')
        try:
            user_id = User.decode_auth_token(token)
            user = User.query.filter(id=user_id)
            return jsonify(message="Valid token", name=user.name)


        except jwt.ExpiredSignatureError:
            return jsonify(message="Token expired")
        except jwt.InvalidSignatureError:
            return jsonify(message="Invalid token")