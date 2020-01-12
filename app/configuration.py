class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../DB/mirror.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_FRAME = False
    FACE_DETECTION_MISSED_HITS = 10
    FACE_RECOGNITION_THRESHOLD = 45
    WEATHER_URL = 'http://dataservice.accuweather.com/'
    WEATHER_API_KEY = 'N9GVHHIxPTogsJx1KXDSNmPurEvmJw1H'
