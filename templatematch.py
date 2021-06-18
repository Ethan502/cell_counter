import cv2 as cv
import numpy as np

def matcher(img_data, template):

    output = img_data.copy()

    if len(img_data.shape) >= 3:
        gray = cv.cvtColor(img_data, cv.COLOR_BGR2GRAY)
    else:
        gray = img_data


    #blur the image
    k = (20,20)
    blurred_gray = cv.blur(gray,k)
    blurred_temp = cv.blur(template,k)

    res = cv.matchTemplate(blurred_gray, blurred_temp, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = list(np.where(res >= threshold))
    
    whys = []
    exes = []
    for pt in zip(*loc[::-1]):
        x,y = pt
        exes.append(x)
        whys.append(y)

    #make the indexes list of non-duplicate x-values
    indexes = []
    doubles = []
    for i in exes:
        if i not in doubles:
            doubles.append(i)
            temp = exes.index(i)
            indexes.append(temp)

    

    #seperate find the correct x and y values at their indexes
    new_xs =[]
    for partx in indexes:
       temp =  exes[partx]
       new_xs.append(temp)

    new_ys =[]
    for party in indexes:
       temp2 =  whys[party]
       new_ys.append(temp2)

    #stitch the points together into the array
    newpts = []
    for spot in range(0,len(indexes)):
        x = new_xs[spot]
        y = new_ys[spot]
        newpt = x, y
        newpts.append(newpt)

    # counter = 0
    # for part in newpts[::-1]:
    #     cv.rectangle(output, part, (part[0] + w, part[1] + h), (0,0,0),1)
    #     cv.circle(output,part,4,(0,0,255),2)
    #     counter = counter + 1

    # doc1 = open('old.txt', 'w')
    # doc2 = open('new.txt', 'w')
    
    # doc1.write(str(newpts))
    # doc2.write(str(new_xs))
    
    # cv.rectangle(output, pt, (pt[0] + w, pt[1] + h), (0,0,0), 1)

    # output = cv.resize(output, (0,0), fx = 0.75, fy= 0.75)
    # cv.imshow('window', output)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    return newpts