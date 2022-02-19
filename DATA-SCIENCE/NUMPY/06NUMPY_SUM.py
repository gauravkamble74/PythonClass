import numpy as np

arr = np.array([1,2,3,4,5])

s = sum(arr)
print(s)

print('-'*30)
print('numpy array product')
# p = prod(arr)
# print(p)

print('-'*30)
print('addition')
a = np.add(1,2)
print(a)

print('-'*30)
print('substarac')
d = np.subtract(5,2)
print(d)

print('-'*30)
print('power operation')
arr1 = [1,2,3,4,5]
arr2 = [2,2,2,2,2]

x = np.float_power(arr1,arr2)
print(x)