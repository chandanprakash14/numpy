import numpy as np
#integer
a=np.array([34,2,4])
print(a.dtype)
#float
b=np.array([1.3,4.9,2.9])
print(b.dtype)
print(b)
#change float to integer
b=np.array([1.3,4.9,2.9],dtype=int)
print("After change float to integer")
print(b)
print(b.dtype)
#String 
n=np.array(['riya','diya','tiya','prithiv'])
print(n.dtype)
#convert int to string 
a=np.array([3,4,2,5],dtype=str)
print(a)
#complex
a=np.array(
    [2 + 4j,4 + 9j]
    )
print(a,a.dtype)