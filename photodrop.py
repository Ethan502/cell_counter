import cv2 as cv
import numpy as np

from counters import circlecounter, cornercounter
from templatematch import matcher
from filter import filter
from threshold import thresholder


img = cv.imread('static/images/cellz.jpg',0)
template = cv.imread('static/images/onecell.jpg',0)

thresholder(img)


