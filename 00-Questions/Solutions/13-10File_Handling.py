# 1. Write a program to read the text from a given file
# 'poems.txt' and find out whether it contains the word 'twinkle'


# with open('poems.txt') as f:
#     content = f.read()

# if 'twinkle' in content:
#     print('Twinkle is present in the file')
# else:
#     print('Twinkle is not present in the file')

# 2.Write a program to generate multiplication table from 2 to 20 and
# write it to the diffrent files. Place these files in a folder

# for i in range(2,21):
#     with open(f'Multiplication/Table_No_{i}.txt','w') as f:
#         for j in range(1,11):
#             f.write(f"{i}X{j}={i*j}\n")

# 3. A file contains a word "Donkey" multiple times. you ned to write 
# a program which replaces this with ###### by updating the same file

# with open('poems.txt') as f:
#     content = f.read()

# content = content.replace('donkey','@#$$@@#')    

# with open('poems.txt','w') as f:
#     f.write(content)

