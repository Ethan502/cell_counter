import cv2 as cv
import numpy as np

from counters import circlecounter, cornercounter

img = cv.imread('static/images/circles.jpg')

circlecounter(img)
