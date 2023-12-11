import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b=a[2,:]
# print(b)
print(a)

b[1]= 100
# print(b)
print(a)