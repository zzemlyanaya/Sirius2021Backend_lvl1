from flask import redirect, request, json
from app import app
from db.url import Url


@app.route('/')
def home():
    return 'Hello there!'


@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.args.get('urlToShorten')
    url = Url(long_url=long_url)
    short_url = url.shorten()
    return json.jsonify({'status': 'Created', 'shortenedUrl': short_url})


@app.route('/<url>', methods=['GET'])
def redirect(url):
    m_url = Url.query.filter_by(short_url=url).first()
    if m_url is None:
        return json.jsonify({'Error': 'Unknown URL'})
    redirect(m_url.get_long_url(), code=301)


@app.route('/<url>/views', methods=['GET'])
def views(url):
    m_url = Url.query.filter_by(short_url=url).first()
    if m_url is None:
        return json.jsonify({'viewCount': 'None'})
    return json.jsonify({'viewCount': m_url.get_views()})
