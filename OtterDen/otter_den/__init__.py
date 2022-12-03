# Copyright ByteOtter (c) 2021-2022

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from otter_den.config import Config

#TODO: if database is not present. Have the app create a database file.

# create SQLAlchemy database instance
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # pass application to all extensions
    #-> No application specific config is stored on the extensions so mulitple configs can be used
    #-> allows to create multiple instances of the app with different configs
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # import Blueprint instances
    from otter_den.users.routes import users
    from otter_den.posts.routes import posts
    from otter_den.main.routes import main
    # register error handlers with application
    from otter_den.errors.handlers import errors
    # register Blueprints to app
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
