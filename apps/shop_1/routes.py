from app import api
from views import *


api.add_resource(HelloWorld, '/api/v1/')
