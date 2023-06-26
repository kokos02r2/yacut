from flask import jsonify, request
from re import match

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .helpers import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса', 400)
    if 'url' not in data or not data['url']:
        raise InvalidAPIUsage('\"url\" является обязательным полем!', 400)
    if not match(
            r'^[a-z]+://[^\/\?:]+(:[0-9]+)?(\/.*?)?(\?.*)?$', data['url']):
        raise InvalidAPIUsage('Указан недопустимый URL')
    short_url = data.get('custom_id')
    if short_url:
        if not match(r'^[A-Za-z0-9]{1,16}$', short_url):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', 400)
        if URLMap.query.filter_by(short=short_url).first():
            raise InvalidAPIUsage(f'Имя "{short_url}" уже занято.', 400)
    else:
        short_url = get_unique_short_id()
    long_url = URLMap.query.filter_by(original=data['url']).first()
    if not long_url:
        long_url = URLMap(original=data['url'])
    long_url.short = short_url
    db.session.add(long_url)
    db.session.commit()
    return jsonify({
        'url': data['url'],
        'short_link': request.host_url + short_url
    }), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url.original}), 200
