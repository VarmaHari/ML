import numpy as np

a=np.array([1,2,3,4,5])
b=np.array([5,6,8,90,44])

c=np.concatenate((a,b))

d=np.concatenate((a,b), axis=0)


print(c)
print(d)