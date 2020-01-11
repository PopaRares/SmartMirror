from flask import render_template
from app import app
from datetime import datetime

@app.route('/')
@app.route('/mirror')
def index():
    user = {'username': 'Rares'}
    date = datetime.now()
    font_url = 'https://fonts.googleapis.com/css?family=Montserrat&display=swap'
    return render_template('mirror.html', user=user, date=date, font_url="https://fonts.googleapis.com/css?family=Montserrat&display=swap")
