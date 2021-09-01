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

    stop_signs = functions.detectAndDisplay(frame, stop_cascade)
    traffic_lights = functions.detectAndDisplay(frame, traffic_cascade)

    num_of_detected_stop_signs = len(stop_signs)
    num_of_detected_traffic_lights = len(traffic_lights)

    # print(str(num_of_detected_stop_signs) + ", " + str(num_of_detected_traffic_lights))

    if num_of_detected_stop_signs > 0:
        for object in stop_signs:
            functions.distanceToObject(object, 70, 500, frame)

    if cv.waitKey(10) == 27:
        break
