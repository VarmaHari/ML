import numpy as np

a=np.random.randint(7, size=(3,3))
# print(a)

b=np.arange(9)
c=np.reshape(b, (3,3))

tr=np.transpose(c)
print(b)
print(c)
print(tr)
