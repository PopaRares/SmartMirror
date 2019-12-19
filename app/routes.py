from app import app

@app.route('/')
@app.route('/mirror')
def index():
    return "Hello, World!"