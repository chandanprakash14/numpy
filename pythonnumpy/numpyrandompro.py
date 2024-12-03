import numpy as np
a=np.random.randint(4)
print(a)
print("----------------------------")
#one dim random
one=np.random.randint(10,size=(1))
print("size",one.ndim)
print(one)
print("----------------------------")
#two dim random
two=np.random.randint(100,size=(2,2))
print("size",two.ndim)
print(two)
three=np.random.randint(100,size=(2,1,2))
print("size",three.ndim)
print(three)

