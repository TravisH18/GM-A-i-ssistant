from sanic.config import Config

class MyConfig(Config):
    DB_NAME = 'dbname'
    DB_HOST = 'localhost'
    DB_NAME = 'appdb'
    DB_USER = 'appuser'