import threading

from app import app
from face_detection import faces
from apiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow


class Mirror:

    has_face = False

    def __init__(self):
        self.mirror_web = threading.Thread(target=app.run, daemon=True, name='web')
        self.face_detect = threading.Thread(target=faces.detect, name='face_detect')
        self.mirror_web.start()
        self.face_detect.start()

        scopes = ["https://www.googleapis.com/auth/calendar.readonly"]

        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
        flow.run_console()


m = Mirror()



