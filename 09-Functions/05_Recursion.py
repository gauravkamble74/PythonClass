def simple_factorial(num):
    factorial=1
    for i in range(1,num):
        factorial = factorial*(i+1)
    return factorial        

def recursive_factorial(num):
    if num==0 or num==1:
        return 1
    return num * recursive_factorial(num-1)    

# f1 = simple_factorial(5)
f1 = recursive_factorial(5)
print(f1)    