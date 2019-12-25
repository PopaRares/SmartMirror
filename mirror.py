import threading

from app import app
from face_detection import faces

test = 5

mirror_web = threading.Thread(target=app.run, daemon=True, name='web')
face_detect = threading.Thread(target=faces.detect, name='face_detect')
mirror_web.start()
face_detect.start()
