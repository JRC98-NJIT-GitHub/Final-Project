from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask_sqlalchemy import SQLAlchemy

from . import view

db = SQLAlchemy()
mysql = MySQL(cursorclass=DictCursor)

def init_app():
    """Initialize the core finalproject."""
    app = Flask(__name__)

    app.config.from_object('config.Config')

    # Initialize Plugins
    mysql.init_app(app)
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        from .view import routes

        # Register Blueprints
        from .view.routes import view_bp
        app.register_blueprint(view_bp)

        return app