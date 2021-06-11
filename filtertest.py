import numpy as np

tester = [1,1,1,1,1,3,4,5,5,6,7,7,7,7,7,8,9,9,9,9,0,0,]
final = []

tester = np.uint64(tester)

final = set(tester)

print(final)