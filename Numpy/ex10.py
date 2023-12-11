import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b=np.nonzero(a<5)
print("nonzero: ", b)

nonzero_list_coordinates= list(zip(b[0],b[1]))
print("the list: ", nonzero_list_coordinates)
