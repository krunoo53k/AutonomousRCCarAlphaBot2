import cv2 as cv
import argparse
import os
import functions

cap = cv.VideoCapture(0)
stop_cascade = cv.CascadeClassifier(os.path.join(os.getcwd(), "haarcascades/stop_sign.xml"))
traffic_cascade = cv.CascadeClassifier(os.path.join(os.getcwd(), "haarcascades/traffic_light.xml"))

while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    num_of_detected_stop_signs = functions.detectAndDisplay(frame, stop_cascade)
    num_of_detected_traffic_lights = functions.detectAndDisplay(frame, traffic_cascade)
    print(str(num_of_detected_stop_signs)+", "+str(num_of_detected_traffic_lights))
    if cv.waitKey(10) == 27:
        break
