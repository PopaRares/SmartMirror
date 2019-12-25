import cv2 as cv


def detect():
    face_cascade = cv.CascadeClassifier('face_detection/cascades/haarcascade_frontalface_alt.xml')

    cap = cv.VideoCapture(0)
    color = (255, 0, 0)  # blue
    text_color = (0, 0, 255)
    stroke = 2
    threshold = 45

    while True:
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]  # region of interest
            end_x = x + w
            end_y = y + h
            cv.rectangle(frame, (x, y), (end_x, end_y), color, stroke)

        cv.imshow('frame', frame)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
