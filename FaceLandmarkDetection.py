import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        # x1 = face.left()
        # y1 = face.top()
        # x2 = face.right()
        # y2 = face.bottom()
        # cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
        landmarks = predictor(gray, face)
        for i in range(17, 68):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            cv2.circle(frame, (x, y), 6, (255, 0, 0), -1)

    cv2.imshow("Frame", frame)
    # time.sleep(60)
    key = cv2.waitKey(1)
    if key == 27:
        break
