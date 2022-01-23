from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#secret key for tampering protection. 256 Bit python key from secrets module. THIS IS NOT A GOOD ENOUGH OF A SOLUTION.
app.config['SECRET_KEY'] = '7e71d5735808a54d9a38d1ebc573ac1429242e464f7f322413a2c8e44392d37d11827c8792c81ca3ccc5cab4bbd5f2d3442823e6919ff74e3339199bd143e81da2e83ff986b2965742ae9b900b1811226b93b01d85ae3d86dd6f5ba6e7aea85d08bc6998f90402310c0ba86519a4d8d56eb5fb1bdcab1e90dc54cfde0164c89f60eeb198c74c813f3eb3e165e767f0d47aa8b1ba33c3fbe6461dc151430f7d46a5480306f87aaae953f5e2570d28663b6100ff06ed7c494c5cadcdac79b03d175288da284e327eab7c38f52b41a641176c66ece2b7083d180f7353f52adb42d6f897801c2639c1a5d6224db8b54985e5410e70b6e198c19de8fa549b474d1e43'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logBlogDEV.db'
#create SQLAlchemy database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from logblog import routes
