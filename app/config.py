class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///appDB.db'
    SECRET_KEY = '****Hello**World!*****'
    PORT = 5000


def get_port():
    return Config.PORT
