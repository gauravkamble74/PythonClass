import numpy as np
import matplotlib.pyplot as pl

arr = np.random.randint(5,15,6)
print(arr)

arrsq = np.square(arr)

print(arrsq)

pl.plot(arr,arrsq)
pl.scatter(arr,arrsq)
pl.xlabel('Number')
pl.ylabel('Squares')
pl.show()