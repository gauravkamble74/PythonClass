# 1. Write a program to print multiplication table of
#    a given number using for loop as well as while loop.


# num = int(input("Enter the number\n"))

# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# Write a program to get all the names in the list that start with a and greet them
# lst = ['anuj','rahul','gaurav','abhi','avinash','pranay']
# for i in lst:
#     if i.startswith('a'):
#         print('hello ' + i)
# 
# 4. Write a program to find sum of first n natural numbers using while loop.
# num = int(input("Enter the number\n"))
# sum = 0
# for i in range(num+1):
#     sum = sum+i
# print(sum)        

# Write a program to find whether a given number is prime or not.

# num = int(input("Enter the number\n"))
# prime = True

# for i in range(2,num+1):
#     if num%i == 0:
#         prime=False
#     else:
#         prime=True

# if prime:
#     print('this is a prime number')
# else:
#     print('this not a prime number')    

# 5. Write a program to calculate the factorial of a given number using for loop.

# num = int(input("Enter the number\n"))

# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i

# print(f"the factorial of {num} is {factorial}")

# start-pattern

# n = 4

# for i in range(n):
#     print("*"*(i+1))

# n=4

# for i in range(n):
#     print(" "*(n-i-1),end="")
#     print("*"*(i*2+1))

# 9. Write a program to print multiplication table of n using for loop in reverse order.

# num = 5
# i=10
# while i < 11 and i>0:
#     print(f"{num} X {i} = {num*i}")
#     i = i-1