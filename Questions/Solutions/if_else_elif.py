# 1. Ask user to enter his age if he is more than 18 yrs old , print you are allowed to enter.

# age = int(input('enter your age'))

# if age>=18:
#     print('you are allowed to enter')
# else:
#     print('you are not allowed to enter')


# 2. Write program to find greatest of 4 number entered by user.

# num1 = int(input('enter 1st no\n'))
# num2 = int(input('enter 2nd no\n'))
# num3 = int(input('enter 3rd no\n'))
# num4 = int(input('enter 4th no\n'))

# print('greates number is')

# if num1>num4:
#     f1 = num1
# else:
#     f1 = num4

# if num2>num3:
#     f2 = num2
# else:
#     f2 = num3     

# if f1>f2:
#     print(f1)
# else:
#     print(f2)    

# 3. Write a program to find out whether the student is pass or fail if it requires total 40% & atleast 33% in each subject 
#    to pass.Take marks of 3 subject input from user


# sub1 = int(input('enter marks of 1st subject'))
# sub2 = int(input('enter marks of 2nd subject'))
# sub3 = int(input('enter marks of 3rd subject'))

# if(sub1<33 or sub2<33 or sub3<33):
#     print('you are failed because youve scored less than 33percent in one of 3 subjec')
# elif (sub1+sub2+sub3)/3 < 40:
#     print('you are failed because total score is less than 40 percent')
# else:
#     print('congratulations youve passed')        

# 4. Write a program to detect spam message.
#    Generally text containing keyword "make lot of money" , "25 din me paisa double" , "buy now limited time offer"
#    "never miss such a chance"

# text = input('enter your message\n')

# if "make lot of money" in text:
#     spam = True
# elif "25 din me paisa double" in text:
#     spam = True
# elif "buy now limited time offer" in text:
#     spam = True
# elif "never miss such a chance" in text:
#     spam=True
# else:
#     spam = False

# if spam==True:
#     print('this is a spam')
# else:
#     print('this is not a spam')    

# 5. Write a program to find whether a given string is present in list or not.

# names = ['dia','siddhi','tanu','pratiksha']

# n = input('enter your name')

# if n in names:
#     print('your name is in list')
# else:
#     print('your name is not in the list')    

# 6. Write a program to find if a post is telling about "girls" or not.

# text = input('enter your text')

# if "girls" in text:
#     print('this text is talking about girls')
# else:
#     print('this post is not talking about girls')    

