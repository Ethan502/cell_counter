import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

highblack = np.array([105,115,255])
lowblack = np.array([0,0,255])


frame = cv.imread('static/images/soccer_practice.jpg')

hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
mask =  cv.inRange(hsv, lowblack, highblack)
#cv.imshow('window', mask)
print(len(mask.shape))
print(len(hsv.shape))

contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in contours:
    area = cv.contourArea(c)
    if area > 400:
        cv.drawContours(frame, c, -1, (255,0,0),2)

frame = cv.resize(frame, (0,0), fx=0.75, fy = 0.75)
cv.imshow('frame', frame)
cv.waitKey(0)
cv.destroyAllWindows()
