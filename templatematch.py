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

    #make the indexes list of non-duplicate x-values
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

    #seperate find the correct x and y values at their indexes
    new_xs =[]
    for partx in indexes:
       temp =  exes[partx]
       new_xs.append(temp)

    new_ys =[]
    for party in indexes:
       temp2 =  whys[party]
       new_ys.append(temp2)


    print(len(indexes))
    print(len(new_xs))

    print(len(new_ys))





    



    

    
    # cv.rectangle(output, pt, (pt[0] + w, pt[1] + h), (0,0,0), 1)

    #output = cv.resize(output, (0,0), fx = 0.75, fy= 0.75)
    cv.imshow('window', output)
    cv.waitKey(0)
    cv.destroyAllWindows()