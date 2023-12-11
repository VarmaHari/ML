import numpy as np


b=np.random.randint(9, size=(3,3))
print("the array: ",b)

c=np.transpose(b)
print("the transpose: ",c)

d=np.flip(c)
print("the reversed array:",d)