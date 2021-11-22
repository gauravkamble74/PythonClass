import numpy as np

print('creating numpy array using list')
lst = [1,2,3,4,5]
arr = np.array(lst)
print(arr)
print(lst)

print('-'*30)
print('types of list and numpy array')
print(type(arr))
print(type(lst))

print('-'*30)
print('shape of numpy array')
arr1 = np.array(([1,2,3,4,5],[6,7,8,9,10]))
print(arr1)
print(arr1.shape)

print('-'*30)
print('length of array')
print(len(arr))
print(len(arr1))