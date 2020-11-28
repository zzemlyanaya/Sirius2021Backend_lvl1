from .init_db import db
import shortuuid as s_id
from app.config import get_port


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(128), unique=True, nullable=False)
    short_url = db.Column(db.String(128), unique=True, nullable=True)
    views = db.Column(db.Integer)

    def shorten(self):
        short_url = s_id.ShortUUID().random(length=10)
        self.short_url = f'http://localhost:{get_port()}/{short_url}'
        return short_url

    def get_short_url(self):
        return self.short_url

    def get_long_url(self):
        return self.long_url

    def get_views(self):
        return self.views

    def add_views(self):
        self.views += 1
