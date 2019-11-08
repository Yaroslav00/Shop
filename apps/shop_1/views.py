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