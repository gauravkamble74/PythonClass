import numpy as np

print('create array using arange()')
arr = np.arange(1,10,2,dtype='int')
print(arr)

print('-'*30)
print('type of array')
print(type(arr[0]))
print(type(arr))

print('-'*30)
print('linear spacing')
arr1 = np.linspace(1,10,3,dtype=int)
print(arr1)

