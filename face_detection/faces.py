import cv2 as cv

import shared_data as shared


def detect():
    face_cascade = cv.CascadeClassifier('face_detection/cascades/haarcascade_frontalface_alt.xml')
    profile_cascade = cv.CascadeClassifier('face_detection/cascades/haarcascade_profileface.xml')

    cap = cv.VideoCapture(0)
    color = (255, 0, 0)  # blue
    color2 = (0, 255, 0)  # blue
    threshold = 10
    hits = 0
    has_face = False

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
            if hits >= threshold:
                has_face = False
        else:
            hits = 0
            has_face = True

        shared.face = has_face

        draw_rectangle((255, 0, 0), faces, gray, frame)
        draw_rectangle((0, 0, 255), profile, gray, frame)
        draw_rectangle((0, 0, 255), profileFlipped, grayFlipped, frame)  # should be flipped?

        cv.imshow('frame', frame)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


def draw_rectangle(color, detection, feed, frame):
    for (x, y, w, h) in detection:
        roi_gray = feed[y:y + h, x:x + w]  # region of interest
        end_x = x + w
        end_y = y + h
        cv.rectangle(frame, (x, y), (end_x, end_y), color, 2)
