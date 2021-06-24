import numpy as np
import cv2 as cv

img = cv.imread('static/images/cellz.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred = cv.GaussianBlur(gray, (5,5),0)

value, thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY_INV)

contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0,0,255), 2)

img = cv.resize(img, (0,0), fx=0.5, fy = 0.5)
cv.imshow('window', thresh)
cv.waitKey(0)
cv.destroyAllWindows