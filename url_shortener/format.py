import re

from flask import (
    Blueprint, flash, render_template, request
)

from .db import get_db

bp = Blueprint('format', __name__, url_prefix='/format')
URL_REGEX = '(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]'
URL_REGEX += '[a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https'
URL_REGEX += '?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})'


@bp.route('/formatter', methods=('GET', 'POST'))
def formatter():
    if request.method == 'POST':
        url = request.form['url']
        url = url.strip('\/')
        db = get_db()
        error = None

        if not url:
            error = 'url is required.'
        elif not re.match(URL_REGEX, url):
            error = 'url is required. not random stuff'
        else:
            new_url = db.execute(
                'SELECT word FROM word WHERE for_url = ?', (url,)
            ).fetchone()
            if new_url:
                return render_template('format/formatter.html', urls={'old_url': url, 'url': new_url['word']})

        if error is None:
            after_slash = url.rpartition('/')[2]
            available_word = None
            index_of_letter = 0
            print("%s" % after_slash[index_of_letter])
            while available_word is None and len(after_slash) > index_of_letter:
                print("%s" % after_slash[index_of_letter])
                available_word = db.execute(
                    "SELECT word FROM word WHERE used=0 AND word LIKE ?",
                    ('{0}%'.format(str(after_slash[index_of_letter])),)
                ).fetchone()
                index_of_letter += 1

            if len(after_slash) <= index_of_letter:
                error = 'no available words'
            else:
                db.execute(
                    "UPDATE word SET used = 1, for_url = '{0}'  WHERE word = '{1}'".format(url, available_word['word'])
                )
                db.commit()
                return render_template('format/formatter.html', urls={'old_url': url, 'url': available_word['word']})

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
