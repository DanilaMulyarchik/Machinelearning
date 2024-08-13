import cv2
import numpy as np

can = cv2.VideoCapture(0)
can.set(0, 300)
can.set(0, 400)
side = 200
text = '1234'
color = (255, 255, 255)
while True:
    success, img = can.read()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('fases.xml')

    res = faces.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in res:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 1)

    cv2.imshow('res', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break