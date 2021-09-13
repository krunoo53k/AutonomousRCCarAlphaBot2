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
        global str_input
        str_input = s.recv(1024).decode()
        print(str_input)
        if str_input == "Bye" or str_input == "bye":
            break


def moveRobot():
    try:
        global str_input
        print("Moving to: "+str_input)
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


t1 = threading.Thread(target=getServerInput)
t2 = threading.Thread(target=moveRobot)

t1.start()
t2.start()

t1.join()
t2.join()