import numpy as np
import cv2
import serial
import time

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

cap=cv2.VideoCapture(0)
port = serial.Serial("/dev/rfcomm0", baudrate=9600)
clear = 5
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes=eye_cascade.detectMultiScale(gray,1.3,5)
 

    for(x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+h]
        roi=frame[y:y+h,x:x+h]
        cv2.imshow("ROi",roi)
        rows, cols, _ = roi.shape
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
        cv2.line(roi, (int(w/2)-clear, 0), (int(w/2)-10, rows), (0, 0, 255), 2)
        cv2.line(roi, (int(w/2)+10, 0), (int(w/2)+10, rows), (0, 0, 255), 2)
        _, threshold = cv2.threshold(gray_roi, 20, 255, cv2.THRESH_BINARY_INV)
        contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)

            cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
            M = cv2.moments(cnt)
            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            except:
                cX = 300
                cY = 300
            print(cX)
            if cX >x +int(w/2)-10 and cX<x+int(w/2)+10 :
                port.write(b'3')
            elif cX>x+int(w/2)+10:
                port.write(b'1')
                # rcv = port.readline()
                # if rcv:
                #     print(rcv)
            elif cX<x+int(w/2)-10:
                port.write(b'2')
                # rcv = port.readline()
                # if rcv:
                #     print(rcv)
            break
        break
    try:
        cv2.imshow("thresh",threshold)
    except:
        cv2.imshow("thresh",np.zeros((300,300),np.uint8))
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
            break       
    

   

cap.release()
cv2.destroyAllWindows()