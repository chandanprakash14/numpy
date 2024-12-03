import numpy as np
#one dim
one=np.array([2,24,234,4])
print(one[3])
print(one[:-1])
#two dim
two=np.array([
    [12,2,4,5],
    [2,34,5,6]
])
print(two[0,2])
#three dim
three=np.array([
    [
        [2,3,4,5,6,9],
        [9,7,5,4,3,2]
    ],
    [
        [2,3,4,5,9,44],
        [4,5,3,2,1,8]
    ]
])
print(three[1,1,3])