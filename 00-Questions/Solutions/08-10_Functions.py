# def greatestNum(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             print(str(num1)+ " is greatest")
#         else:
#             print(str(num3)+ " is greatest")            
#     else:
#         if num2>num3:
#             print(str(num2)+" is greatest")
#         else:
#             print(str(num3)+" is greatest")


# greatestNum(6,1,3)

# 7. Write a python function to remove a given word from a string and strip it at the same time


def remove_and_strip(sen,text):
    x = sen.replace(text,"")
    return x.strip()
    

sentence = "               you girls seem pretty smart           "

s = remove_and_strip(sentence,"smart")
print(s)