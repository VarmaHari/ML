import numpy as np
a=np.array([1,2,3,4,5,6])
a.shape
print(a.shape)

a2=a[np.newaxis, :]
print(a2.shape)
