class Check:
    def __init__(self):
        print('Address of self is =',id(self))

obj = Check()
ojb1 = Check()
print('Address of obj is ',id(obj))
print('Address of obj1 is ',id(ojb1))