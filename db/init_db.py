from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


def init_db():
    from .url import Url
    db.create_all()