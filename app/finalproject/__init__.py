from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

mysql = MySQL(cursorclass=DictCursor)

def init_app():
    """Initialize the core finalproject."""
    app = Flask(__name__)

    app.config.from_object('config.Config')

    # Initialize Plugins
    mysql.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes

        # Register Blueprints
#        app.register_blueprint(auth.auth_bp)
#        app.register_blueprint(admin.admin_bp)

        return app