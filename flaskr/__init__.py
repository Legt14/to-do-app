from flask import Flask, url_for, redirect
from flask_login import LoginManager

from .config import Config
from .auth import bp
from .crud import get_user_tasks
from .models import UserModel



login_manager = LoginManager()
login_manager.blueprint_login_views = {'login_view': 'auth.login'}


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query(user_id)


def create_app():    
    app = Flask(__name__)
    app.config.from_object(Config)
    login_manager.init_app(app)
    app.register_blueprint(bp.auth)
    
    return app
