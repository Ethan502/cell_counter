import cv2 as cv
import numpy as np

def matcher(img_data, template):

    output = img_data.copy()

    if len(img_data.shape) >= 3:
        gray = cv.cvtColor(img_data, cv.COLOR_BGR2GRAY)
    else:
        gray = img_data

    w,h = template.shape[::-1]

    k = (20,20)
    blurred_gray = cv.blur(gray,k)
    blurred_temp = cv.blur(template,k)

    res = cv.matchTemplate(blurred_gray, blurred_temp, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv.rectangle(output, pt, (pt[0] + w, pt[1] + h), (0,0,0), 1)

    #output = cv.resize(output, (0,0), fx = 0.75, fy= 0.75)
    cv.imshow('window', output)
    cv.waitKey(0)
    cv.destroyAllWindows()