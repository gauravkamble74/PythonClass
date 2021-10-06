# 1. Write a program to print multiplication table of
#    a given number using for loop as well as while loop.


# num = int(input("Enter the number\n"))

# i=1

# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")


# Write a program to find whether a given number is prime or not.

# num = int(input("Enter the number\n"))
# prime = True

# for i in range(2,num):
#     if num%2 == 0:
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

# n = 3

# for i in range(n):
#     print("*"*(i+1))

n=3

for i in range(n):
    print(" "*(n-i),end="")
    print("*"*(i*2+1))