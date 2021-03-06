import cv2 as cv
import pickle
from app import Config, Shared
from app.user import User

def detect():
    face_cascade = cv.CascadeClassifier('face_detection/cascades/haarcascade_frontalface_alt.xml')
    profile_cascade = cv.CascadeClassifier('face_detection/cascades/haarcascade_profileface.xml')

    recogniser = cv.face.LBPHFaceRecognizer_create()
    recogniser.read("face_detection/trainer.yml")

    face_ids = {}
    with open("face_detection/labels.pkl", "rb") as f:
        og_labels = pickle.load(f)
        face_ids = {v: k for k, v in og_labels.items()}

    cap = cv.VideoCapture(0)
    hits = 0
    face_id = 0
    while True:
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        grayFlipped = cv.flip(gray, 1)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        profile = profile_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        profileFlipped = profile_cascade.detectMultiScale(grayFlipped, scaleFactor=1.5, minNeighbors=5)

        # no face
        if isinstance(faces, tuple) and isinstance(profile, tuple):
            hits = hits + 1
            if hits >= Config.FACE_DETECTION_MISSED_HITS:
                Shared.FACE_EXISTS = False
        else:
            hits = 0
            Shared.FACE_EXISTS = True

            recogniser_id, conf = recogniser.predict(gray)
            if conf >= Config.FACE_RECOGNITION_THRESHOLD:
                face_id = face_ids[recogniser_id]
            else:
                face_id = 0

        if face_id != Shared.FACE_ID:
            Shared.FACE_ID = face_id
            Shared.CURRENT_USER = User.query.get(face_id)

        draw_rectangle((255, 0, 0), faces, gray, frame)
        draw_rectangle((0, 0, 255), profile, gray, frame)
        draw_rectangle((0, 0, 255), profileFlipped, grayFlipped, frame)  # should be flipped?

        if Config.SHOW_FRAME:
            cv.imshow('frame', frame)
            if cv.waitKey(20) & 0xFF == ord('q'):
                break

    cap.release()
    cv.destroyAllWindows()


def draw_rectangle(color, detection, feed, frame):
    for (x, y, w, h) in detection:
        end_x = x + w
        end_y = y + h
        cv.rectangle(frame, (x, y), (end_x, end_y), color, 2)
