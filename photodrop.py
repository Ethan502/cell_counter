import cv2 as cv
import numpy as np

from counters import circlecounter, cornercounter
from templatematch import matcher

img = cv.imread('static/images/cellz.jpg')
template = cv.imread('static/images/onecell.jpg',0)

#print("og template type")
#print(type(template))

matcher(img, template)
