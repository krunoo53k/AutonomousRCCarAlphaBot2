import cv2 as cv

def detectAndDisplayStopSigns(frame,stop_cascade):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    stop_signs = stop_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in stop_signs:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
    cv.imshow('Capture - Stop sign detection', frame)
    return len(stop_signs)