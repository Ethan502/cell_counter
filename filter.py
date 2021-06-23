import numpy as np
import cv2 as cv

from templatematch import matcher

def filter(img, template):

    points = matcher(img, template)

    w,h = template.shape[::-1]

    a = 0
    b = 1
    c = 0
    thresh = 30

    finalsA = []

    #filter function
    while True: 

        if b == len(points):
            finalsA.append(points[a])
            break
        
        if abs(points[b][0] - points[a][0]) < thresh:
            b = b + 1

        elif abs(points[b][0] - points[a][0]) > thresh:
            finalsA.append(points[a])
            b = b + 2
            a = b - 1

        if b > len(points):
            finalsA.append(points[a])
            break

        # doc1 = open('originals.txt', 'w')
        # for i in points:
        #     doc1.write(str(i))

        # doc2 = open('new.txt', 'w')
        # for j in finalsA:
        #     doc2.write(str(j))

    counter = 0
    for part in finalsA[::-1]:
        cv.rectangle(img, part, (part[0] + w, part[1] + h), (0,0,0),1)
        cv.circle(img,part,4,(0,0,255),2)
        counter = counter + 1

    print(counter)
    img = cv.resize(img, (0,0), fx = 0.5, fy= 0.5)
    cv.imshow('cells', img)
    cv.waitKey(0)
    cv.destroyAllWindows()