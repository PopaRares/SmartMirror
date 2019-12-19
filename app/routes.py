from flask import render_template

from app import app


@app.route('/')
@app.route('/mirror')
def index():
    user = {'username': 'Rares'}
    font_url = 'https://fonts.googleapis.com/css?family=Montserrat&display=swap'
    return render_template('mirror.html', user=user, font_url=font_url)
