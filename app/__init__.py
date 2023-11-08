from flask import Flask
from .extentions import db, login
from .web.routes import web
from .login_manager import load_user

def create_app():
    app = Flask(__name__)
    app.register_blueprint(web, url_prefix="/")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.secret_key = '123456789'

    login.init_app(app)
    db.init_app(app)

    return app