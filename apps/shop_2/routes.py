from app import api
from views import *


api.add_resource(HelloWorld, '/api/v1/items_count/')
api.add_resource(SignUp, '/api/v1/auth/signup/')
api.add_resource(LogIn, '/api/v1/auth/login/')
api.add_resource(IsAuth, 'api/v1/auth/isauth/')