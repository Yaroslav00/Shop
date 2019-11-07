from app import api
from models import *
from flask_restful import Resource, Api
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
        