import numpy as np

arr=np.array([
    [20,44,45,5],
    [12,4,5,2],
    [7,9,5,4]
])

print(arr)
print(type(arr))

print('-'*30)
print('all rows and 0 and 1 column')
arr1 = arr[:,0:2]
print(arr1)

print('-'*30)
print('rows 1 and 2 with all columns')
arr2 = arr[1:3,:]
print(arr2)

print('-'*30)
print('form row 1 onwards to column 1 onwards')
arr3 = arr[1:,1:]
print(arr3)

print('-'*30)
print('form row 1 take all 0 column values')
print(arr[1:,0])

