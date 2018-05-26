from flask import (
    Blueprint, flash, redirect, render_template, request
)

from url_shortener.db import get_db

bp = Blueprint('redirector', __name__, url_prefix='')


# a simple page that says hello
@bp.route('/')
def hello():
    return 'Hello World!'


@bp.route('/<word>', methods=('GET', 'POST'))
def redirector(word):
    if request.method == 'GET':
        db = get_db()
        error = None

        if not word:
            error = 'word is required.'
        else:
            new_url = db.execute(
                'SELECT for_url FROM word WHERE word = ?', (word,)
            ).fetchone()
            if new_url:
                return redirect(new_url['for_url'])
            else:
                error = 'no such url found.'

        flash(error)

    return render_template('format/formatter.html', urls={'old_url': ''})


@bp.route('/recent', methods=('GET',))
def recent():
    if request.method == 'GET':
        db = get_db()
        urls = db.execute(
            'SELECT word, for_url FROM word WHERE for_url IS NOT NULL'
        ).fetchmany(20)

        return render_template('format/recent.html', urls=urls)

    return render_template('format/recent.html')
