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
    threshold = 0.82
    loc = list(np.where(res >= threshold))
    
    
    exes = []
    for pt in zip(*loc[::-1]):
        y,x = pt
        exes.append(x)

    indexes = []
    doubles = []
    for i in exes:
        if i not in doubles:
            doubles.append(i)
            temp =  exes.index(i)
            indexes.append(temp)

    whys = []
    for point in zip(*loc[::-1]):
        y,x = point
        whys.append(y)

    new_x = []
    for xpart in exes:
        if exes.index(xpart) in indexes:
            new_x.append(xpart)


    new_y = []
    for ypart in whys:
        if whys.index(ypart) in indexes:
            new_y.append(ypart)

    doc2 = open('indexes.txt','w')
    doc = open('exes.txt','w')
    doc3 = open('newexes.txt','w')
    doc4 = open('newys.txt', 'w')

    doc.write(str(exes))
    doc2.write(str(indexes))
    doc3.write(str(new_x))
    doc4.write(str(new_y))

    print(len(exes))
    print(len(new_x))
    print(len(whys))
    print(len(new_y))
    print(len(indexes))




    

    
    # cv.rectangle(output, pt, (pt[0] + w, pt[1] + h), (0,0,0), 1)

    #output = cv.resize(output, (0,0), fx = 0.75, fy= 0.75)
    cv.imshow('window', output)
    cv.waitKey(0)
    cv.destroyAllWindows()