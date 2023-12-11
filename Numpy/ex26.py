# The 1D array creation functions e.g. numpy.linspace and numpy.arange generally need at least two inputs, start and stop.
import numpy as np


np.arange(10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(2, 10, dtype=float)
# array([2., 3., 4., 5., 6., 7., 8., 9.])
np.arange(2, 3, 0.1)
# array([2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])
np.linspace(1., 4., 6)
#array([1. ,  1.6,  2.2,  2.8,  3.4,  4. ])


# The 2D array creation functions e.g. numpy.eye, numpy.diag, and numpy.vander define properties of special matrices represented as 2D arrays. 

a=np.eye(3, dtype=int)
print(a)

b=np.eye(3,5)
print(b)