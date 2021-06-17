import numpy as np
import cv2 as cv

from templatematch import matcher

img = cv.imread('static/images/cellz.jpg')
template = cv.imread('static/images/onecell.jpg',0)

points = matcher(img, template)

starter = points[0][0]

print(starter)