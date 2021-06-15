import numpy as np

tester = [18,53,64,76,32,45,12,1,87]
indexes = [1,0,7,6]
num = []

for pt in tester:
    if tester.index(pt) in indexes:
        num.append(pt)

print(num)
print(indexes[::-1])