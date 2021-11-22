import numpy as np

print('-'*30)
print('numpy array with random integers')
arr = np.random.randint(5,15,5)
print(arr)


print('-'*30)
print('getting a random number from above array')
x = np.random.choice(arr)
print(x)

print('-'*30)
print('shuffel values in the array')
np.random.shuffle(arr)
print(arr)
