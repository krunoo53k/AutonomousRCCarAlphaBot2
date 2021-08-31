import cv2 as cv
import argparse
import os
import functions

cap = cv.VideoCapture(0)
stop_cascade = cv.CascadeClassifier(os.path.join(os.getcwd(), "haarcascades/stop_sign.xml"))


while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    num_of_detected_stop_signs = functions.detectAndDisplayStopSigns(frame, stop_cascade)
    print(num_of_detected_stop_signs)
    if cv.waitKey(10) == 27:
        break
