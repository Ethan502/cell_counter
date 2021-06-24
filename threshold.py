import cv2 as cv
import numpy as np

def thresholder(img):

    print(len(img.shape))

    gray = img.copy()

    gray =  cv.cvtColor(gray, cv.COLOR_BGR2GRAY)

    blank = np.zeros(img.shape, img.dtype)

    retval, threshold = cv.threshold(img, 70, 255, cv.THRESH_BINARY)
    
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1,1))
    morph = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernel)
    morph = cv.morphologyEx(morph, cv.MORPH_OPEN, kernel)
    pic = cv.adaptiveThreshold(morph, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)

    print(len(pic.shape))

    contours, hierarchy = cv.findContours(gray, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(pic, contours, -1, (0,0,255),2)
    
    

    
    
    cv.imshow('original', img)
    cv.imshow('gaus', pic)

    cv.waitKey(0)
    cv.destroyAllWindows()