import cv2 as cv
import numpy as np

def matcher(img_data, template):

    output = img_data.copy()

    if len(img_data.shape) >= 3:
        gray = cv.cvtColor(img_data, cv.COLOR_BGR2GRAY)
    else:
        gray = img_data

    w,h = template.shape[::-1]

    # gray = np.float32(gray)
    # template = np.float32(template)

    res = cv.matchTemplate(gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.75
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv.rectangle(output, pt, (pt[0] + w, pt[1] + h), (0,0,0), 1)

    #output = cv.resize(output, (0,0), fx = 0.75, fy= 0.75)
    cv.imshow('window', output)
    cv.waitKey(0)
    cv.destroyAllWindows()