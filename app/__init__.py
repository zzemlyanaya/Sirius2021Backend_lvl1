from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)


def init_app():
    from db import init_db, url
    init_db()

    from . import routes
