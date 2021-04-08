import cv2
import serial
import numpy as np 

cap = cv2.VideoCapture(0)
port = serial.Serial("/dev/rfcomm2", baudrate=9600)
t=20
second_val=1200
third_val = 4000
while True:
    ret,frame=cap.read()
    cv2.imshow("frame",frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    _, threshold = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)
    non_zero = cv2.countNonZero(threshold)
    print(non_zero)
    if non_zero>0 and non_zero<second_val:
        port.write(b'1')
        print("Right")
    elif non_zero>second_val and non_zero<third_val:
        port.write(b'3')
        print("Forward")
    else:
        port.write(b'2')
        print("Left")
    cv2.imshow("Thresh",threshold)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break  