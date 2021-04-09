import cv2
import numpy as np
import serial
import time

cap = cv2.VideoCapture(0)
#port = serial.Serial("/dev/rfcomm0", baudrate=9600)

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    roi = frame
    rows, cols, _ = roi.shape
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
    cv2.line(roi, (630, 0), (630, rows), (0, 255, 0), 2)
    _, threshold = cv2.threshold(gray_roi, 30, 255, cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        if cX>630:
            #port.write(b'1')
            pass
            # rcv = port.readline()
            # if rcv:
            #     print(rcv)
        else:
            #port.write(b'2')
            pass
            # rcv = port.readline()
            # if rcv:
            #     print(rcv)
        break

    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows()