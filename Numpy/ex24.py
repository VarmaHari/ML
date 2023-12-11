import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 8, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'purple') # line
plt.plot(x, y, 'o')      # dots
plt.show()