import cv2 as cv

img = cv.imread('static/images/circles.jpg')

blurry = cv.blur(img,(20,20))

print(type(blurry))

cv.imshow('window', blurry)
cv.waitKey(0)
cv.destroyAllWindows()
