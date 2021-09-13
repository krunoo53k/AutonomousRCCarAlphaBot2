import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2
import socket
import threading

Ab = AlphaBot2()

TRIG = 22
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)

Ab.setPWMA(30)
Ab.setPWMB(30)

s = socket.socket()
s.connect(('192.168.1.7', 12345))
str_input = "s"


def getServerInput():
    while True:
        str_input = s.recv(1024).decode()
        if str_input == "Bye" or str_input == "bye":
            break


t1 = threading.Thread(target=getServerInput())

try:
    while True:
        if str_input == "s":
            Ab.stop()
            time.sleep(0.3)
        elif str_input == "w":
            Ab.forward()
            time.sleep(0.02)

except KeyboardInterrupt:
    GPIO.cleanup()
    s.close()
