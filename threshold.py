import cv2 as cv
import numpy as np

def thresholder(img):

    blank = np.zeros(img.shape, img.dtype)

    retval, threshold = cv.threshold(img, 70, 255, cv.THRESH_BINARY)
    
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1,1))
    morph = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    morph = cv.morphologyEx(morph, cv.MORPH_OPEN, kernel)
    gaus = cv.adaptiveThreshold(morph, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)


    
    
    
    #cleared = cv.fastNlMeansDenoising(gaus,blank,5,7,21)

    # circles = cv.HoughCircles(gaus, cv.HOUGH_GRADIENT, 1, 30, 6, 50, 30, 0, 0)
    # detected_circles = np.uint16(np.around(circles))

    # for (x,y,r) in detected_circles[0,:]:
    #     cv.circle(gaus, (x,y), r, (0,0,0), 3)


    
    cv.imshow('original', img)
    cv.imshow('window', threshold)
    cv.imshow('gaus', gaus)
    cv.imshow('cleared', morph)

    cv.waitKey(0)
    cv.destroyAllWindows()