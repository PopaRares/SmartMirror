from flask import render_template
from app import app, Shared, weather

data = {}


@app.route('/')
@app.route('/mirror')
def index():
    return render_template('mirror.html', font_url="https://fonts.googleapis.com/css?family=Montserrat&display=swap")


@app.route("/data", methods=['GET'])
def getFace():
    data['isFace'] = Shared.FACE_EXISTS
    if Shared.CURRENT_USER is None:
        data['name'] = "stranger"
    else:
        data['name'] = Shared.CURRENT_USER.name
    return data


@app.route("/weather")
def getWeather():
    location_data = weather.getLocation()
    if location_data is not None and 'Key' in location_data:
        location_key = location_data['Key']
        status = 'SUCCESS'
        data['weather_now'] = weather.getWeatherNow(location_key)
        data['weather_forecast'] = weather.getForecast(location_key)
    else:
        status = 'FAIL'
    print(data)
    ret_msg = {'update': status}
    return ret_msg
