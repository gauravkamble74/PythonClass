import numpy as np
import matplotlib.pyplot as pl

arr = np.arange(1,30,2)
print(arr)

pl.plot(arr,arr,'r--')
pl.plot(arr,arr**2,'ys')
pl.plot(arr,arr**3,'g^')
pl.grid(True)
pl.show()