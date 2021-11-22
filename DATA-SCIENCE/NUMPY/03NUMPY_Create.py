import numpy as np

print('numpy array with all zeroes')
arr0 = np.zeros(10,dtype=int)
print(arr0)

print('-'*30)
print('numpy array with all one')
arr1 = np.ones(10,dtype=int)
print(arr1)

print('_'*30)
print('numpy array with random values')
arr = np.random.random((1,5,2))
print(arr)