# Printing the nth value of fibonacci series 

# 1. using the loops

# def fibonacci(n):
#     a = 0
#     b = 1
    
#     if n<0:
#         print('invalid number')
#     elif n==0:
#         return 0
#     elif n==1:
#         return b
#     else:
#         for i in range(1,n):
#             c = a + b
#             a = b
#             b = c
#         return b   

# x = fibonacci(-1)
# print(x)

# 2. using Recursion 

def fibonacci_recur(n):
    if n<0:
        print('invalid')
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci_recur(n-1)+fibonacci_recur(n-2)

x = fibonacci_recur(9)        
print(2)