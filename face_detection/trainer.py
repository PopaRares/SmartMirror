import cv2 as cv
import os
import numpy as np
import pickle


face_cascade = cv.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')
recogniser = cv.face.LBPHFaceRecognizer_create()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

current_id = 0
label_ids = {}
labels = []
train = []

for root, dir, files in os.walk(image_dir):
    for file in files:
        path = os.path.join(root, file)
        label = os.path.basename(os.path.dirname(path))

        if not label in label_ids:
            label_ids[label] = current_id
            current_id += 1
        id_ = label_ids[label]

        pil_image = Image.open(path).convert("L") #grayscale
        image_array = np.array(pil_image, "uint8")

        face = face_cascade.detectMultiScale(image_array)
        for x, y, w, h in face:
            roi = image_array[y:y+h, x:x+w]
            train.append(roi)
            labels.append(id_)

print(label_ids)

with open("labels.pkl", "wb") as f:
    pickle.dump(label_ids, f)

recogniser.train(train, np.array(labels))
recogniser.save("trainer.yml")