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
str_input = "w"


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


def getServerInput():
    while True:
        global str_input
        str_input = s.recv(1024).decode()
        if str_input == "Bye" or str_input == "bye":
            break


thread1 = threading.Thread(target=getServerInput)
thread1.setDaemon(True)
thread1.start()

try:
    while True:
        if dist() < 25:
            Ab.stop()
            time.sleep(0.3)
        elif str_input == "s":
            Ab.stop()
            print("Stop sign detected, stopping.")
            time.sleep(0.3)
        elif str_input == "w":
            Ab.forward()
        else:
            Ab.stop()
            time.sleep(0.3)
        time.sleep(0.02)
except KeyboardInterrupt:
    GPIO.cleanup()
    thread1.join()
    s.close()



