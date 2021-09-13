import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2
import socket

Ab = AlphaBot2()

TRIG = 22
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)

Ab.setPWMA(30)
Ab.setPWMB(30)


def dist():
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TRIG, GPIO.LOW)
    while not GPIO.input(ECHO):
        pass
    t1 = time.time()
    while GPIO.input(ECHO):
        pass
    t2 = time.time()
    return (t2 - t1) * 34000 / 2


s = socket.socket()
s.connect(('192.168.1.7', 12345))

try:
    while True:
        print("Hello")
        middleDistance = dist()
        print("Distance:%0.2f cm" % middleDistance)
        if middleDistance < 30:
            Ab.stop()
            time.sleep(0.3)
        else:
            Ab.forward()
            time.sleep(0.02)
        print("Distance:%0.2f cm" % dist())
except KeyboardInterrupt:
    GPIO.cleanup()
