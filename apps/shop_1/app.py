from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_socketio import SocketIO
from flask_mail import Mail
application = Flask(__name__)
api  = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1/shop'
db = SQLAlchemy(application)
migrate = Migrate(application, db)
socketio = SocketIO(application)
application.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'yarik.voytovich@gmail.com',
    MAIL_HOST_USER = 'yarik.voytovich@gmail.com',
    MAIL_HOST_PASSWORD = 'khcfqljxebkzhgsq',
   MAIL_PASSWORD = 'khcfqljxebkzhgsq'
)

mail = Mail(application)


    
from routes import *


