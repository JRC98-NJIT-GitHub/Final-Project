from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

from . import view

db = SQLAlchemy()
mysql = MySQL(cursorclass=DictCursor)
login_manager = LoginManager()
sess = Session()

def init_app():
    """Initialize the core finalproject."""
    app = Flask(__name__)

    app.config.from_object('config.Config')

    # Initialize Plugins
    mysql.init_app(app)
    db.init_app(app)
    sess.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        from .view import routes
        from . import auth

        # Register Blueprints
        from .view.routes import view_bp
        app.register_blueprint(view_bp)
        app.register_blueprint(auth.auth_bp)

        return app