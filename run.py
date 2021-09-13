import cv2 as cv
import os
import functions
import socket
import time

# Grab the video stream from bot
cap = cv.VideoCapture("http://192.168.1.11:8080/?action=stream")

stop_cascade = cv.CascadeClassifier(os.path.join(os.getcwd(), "haarcascades/stop_sign.xml"))
traffic_cascade = cv.CascadeClassifier(os.path.join(os.getcwd(), "haarcascades/traffic_light.xml"))

# Connect to the robot through a socket
s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
c, address = s.accept()
print("Socket Up and running with a connection from", address)

lastStopTime = time.time() - 5
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
        rcvdData = c.recv(1024).decode()
    frame = cv.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
    stop_signs = functions.detectAndDisplay(frame, stop_cascade)
    # traffic_lights = functions.detectAndDisplay(frame, traffic_cascade)
    currentTime = time.time()
    num_of_detected_stop_signs = len(stop_signs)
    # num_of_detected_traffic_lights = len(traffic_lights)

    # print(str(num_of_detected_stop_signs) + ", " + str(num_of_detected_traffic_lights))

    if num_of_detected_stop_signs > 0:
        for object in stop_signs:
            if  functions.distanceToObject(object, 70, 500, frame) < 30 and currentTime - lastStopTime >= 3:
                c.send("s".encode())
                time.sleep(5)
                lastStopTime = time.time()
                c.send("w".encode())
    if cv.waitKey(10) == 27:
        c.close()
        break
