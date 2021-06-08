import cv2 as cv
import numpy as np

def circlecounter(img_data):
    
    output = img_data.copy()

    if len(img_data.shape) >= 3:
        gray = cv.cvtColor(img_data, cv.COLOR_BGR2GRAY)
    else:
        gray = img_data

    gray = cv.medianBlur(gray, 5)

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 75, 6, 50, 30, 0, 0)
    detected_circles = np.uint16(np.around(circles))

    for (x,y,r) in detected_circles[0,:]:
        cv.circle(output, (x,y), r, (0,0,0), 3)

    cv.imshow('window', output)
    cv.waitKey(0)
    cv.destroyAllWindows()

def cornercounter(img_data):
    
    output = img_data.copy()

    if len(img_data.shape) >= 3:
        gray = cv.cvtColor(img_data, cv.COLOR_BGR2GRAY)
    else:
        gray = img_data

    corners = cv.goodFeaturesToTrack(gray, 10, 0.5, 20)
    corners = np.float32(corners)

    for item in corners:
        x,y = item[0]
        cv.circle(output, (int(x),int(y)), 10, (0,0,0), 3)
    
    cv.imshow('window', output)
    cv.waitKey(0)
    cv.destroyAllWindows()
    