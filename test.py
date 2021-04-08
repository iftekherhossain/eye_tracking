import cv2
import serial
import numpy as np 

cap = cv2.VideoCapture(0)
port = serial.Serial("/dev/rfcomm4", baudrate=9600)
while True:
    ret,frame=cap.read()
    cv2.imshow("frame",frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    _, threshold = cv2.threshold(blur, 11, 255, cv2.THRESH_BINARY_INV)
    non_zero = cv2.countNonZero(threshold)
    print(non_zero)
    
    cv2.imshow("Thresh",threshold)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break  