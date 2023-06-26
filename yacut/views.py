from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URLForm
from .helpers import get_unique_short_id
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data or get_unique_short_id()
        long_url = URLMap.query.filter_by(original=form.original_link.data).first()
        if not long_url:
            long_url = URLMap(original=form.original_link.data)
        long_url.short = short_url
        db.session.add(long_url)
        db.session.commit()
        flash(url_for('short_view', short=short_url, _external=True))
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def short_view(short):
    return redirect(URLMap.query.filter_by(short=short).first_or_404().original)
