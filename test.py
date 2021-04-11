import cv2
import serial
import numpy as np 

def nothing(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('Thresh Control')
cv2.createTrackbar("Min","Thresh Control",0,255,nothing)
# cv2.createTrackbar("Max","Thresh Control",0,255,nothing)
second_val=1000
third_val = 9000
while True:
    ret,frame=cap.read()
    # frame = frame[220:,:300]
    minimum = cv2.getTrackbarPos("Min","Thresh Control")
    maximum = 255
    cv2.imshow("frame",frame)
    #print(frame.shape)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 1)
    _, threshold = cv2.threshold(gray, minimum, maximum, cv2.THRESH_BINARY_INV)
    # threshold = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,4)
    non_zero = cv2.countNonZero(threshold)
    print(non_zero)
    cv2.imshow("Thresh",threshold)
    if non_zero>=0 and non_zero<second_val:
        print("Right")
    elif non_zero>second_val and non_zero<third_val:
        print("Forward")
    else:
        print("Left")
    cv2.imshow("Thresh",threshold)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break  
