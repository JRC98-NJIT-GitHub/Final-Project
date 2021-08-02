"""Flask configuration."""

class Config:
    MYSQL_DATABASE_HOST = 'db'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'root'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_DB = 'mlbteams'

    MYSQL_DATABASE_HOST = 'db'
    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        MYSQL_DATABASE_USER, MYSQL_DATABASE_PASSWORD, MYSQL_DATABASE_HOST, MYSQL_DATABASE_PORT,MYSQL_DATABASE_DB)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#    FLASK_APP = 'wsgi.py'
    SECRET_KEY = 'GDtfDCFYjD'

    SESSION_TYPE = 'filesystem'
