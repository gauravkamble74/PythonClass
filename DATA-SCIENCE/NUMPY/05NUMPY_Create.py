import numpy as np

# arr = [1-0,2-1,3-2,4-3,5-4]

# arr = np.array(arr)
# print(type(arr))
# print(arr)

arr = np.array([1,2,3,4,5])
print(type(arr))

print('-'*30)
print('values upto 3 elements')
arr1 = arr[:3]
print(arr1)

print('-'*30)
print('values from 3 elements')
arr2 = arr[3:]
print(arr2)

print('-'*30)
print('values from 1 upto 3 elements')
arr3 = arr[1:3]
print(arr3)

print('-'*30)
print('conditional retrival')
arr4 = arr[arr%2==0]
print(arr4)

print('-'*30)
print('conditional status in boolean array')
arr=(arr%2==1)
print(arr)
