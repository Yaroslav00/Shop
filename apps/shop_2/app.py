from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
application = Flask(__name__)
api  = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1/shop'
db = SQLAlchemy(application)
migrate = Migrate(application, db)
from routes import *


