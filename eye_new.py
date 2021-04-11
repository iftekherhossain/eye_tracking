import cv2
import serial
import numpy as np
import RPi.GPIO as GPIO 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
port = serial.Serial("/dev/rfcomm1", baudrate=9600)
t=20
second_val=1000
third_val = 9000
cv2.namedWindow('Thresh Control')
cv2.createTrackbar("Min","Thresh Control",0,30,nothing)
# cv2.createTrackbar("Max","Thresh Control",0,255,nothing)
second_val=1000
third_val = 9000
while True:
    ret,frame=cap.read()
    cv2.imshow("frame",frame)
    minimum = cv2.getTrackbarPos("Min","Thresh Control")
    maximum = 255
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    _, threshold = cv2.threshold(blur, minimum, maximum, cv2.THRESH_BINARY_INV)
    non_zero = cv2.countNonZero(threshold)
    print(non_zero)
    if GPIO.input(10) == GPIO.HIGH: 
        if non_zero>=0 and non_zero<second_val:
            port.write(b'1')
            print("Right")
        elif non_zero>second_val and non_zero<third_val:
            port.write(b'3')
            print("Forward")
        else:
            port.write(b'2')
            print("Left")
    else:
        print("Switch Off!!")
        port.write(b'0')
    cv2.imshow("Thresh",threshold)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break  
