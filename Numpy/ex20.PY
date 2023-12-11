import numpy as np
import pandas as pd

a=np.array([[1,2,3],[5,6,7],[7,8,9]])
np.save('filename',a)

b=np.load('filename.npy')
frame=pd.DataFrame(a)
print(b)
print(frame)