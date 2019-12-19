from flask import render_template

from app import app


@app.route('/')
@app.route('/mirror')
def index():
    user = {'username': 'Rares'}
    return render_template('mirror.html', user=user)
