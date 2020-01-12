import threading

from app import app
from face_detection import faces


class Mirror:

    has_face = False

    def __init__(self):
        self.mirror_web = threading.Thread(target=app.run, daemon=True, name='web')
        self.face_detect = threading.Thread(target=faces.detect, name='face_detect')
        self.mirror_web.start()
        self.face_detect.start()

m = Mirror()



