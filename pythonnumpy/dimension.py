import numpy as np
#zero dimension
a=np.array(2)
print(a.ndim)
print(a.shape)
#one dimension
b=np.array([2,3,4])
print(b.ndim)
print(b.shape)
#two dimension
c=np.array([
    [2,3,4,5],
    [7,8,5,7]
])
print(c.ndim)
print(c.shape)
d=np.array([
    [
        [4],
        [2]
    ],
    [
        [2],
        [4]
    ]
])
print(d.ndim)
print(d.shape)