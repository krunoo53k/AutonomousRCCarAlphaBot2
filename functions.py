import cv2 as cv


def detectAndDisplay(frame, cascade):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    objects_detected = cascade.detectMultiScale(frame_gray, 1.05, 3)
    for (x, y, w, h) in objects_detected:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
    cv.imshow('Capture - Stop sign detection', frame)
    return objects_detected


def distanceToObject(object, widthOfObject, focalLength, frame):
    perceivedWidth = object[3]
    distance = (widthOfObject * focalLength) / perceivedWidth
    # cv.putText(frame, 'Christmas', (200, 200), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv.LINE_AA) ovo ne radi
    # iz nekog razloga?
    print(distance)
