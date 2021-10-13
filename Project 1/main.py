# a program to play rock paper siccsor against computer

import random

def gameWin(comp, you):
        # checks whether computer and user chose the same 
        if comp == you:
            return None

        # checks possibilty of winning or losing of user 
        elif comp == 'r':
            if you=='p':
                return False
            elif you=='s':
                return True

        # checks possibilty of winning or losing 

        elif comp == 'p':
            if you=='r':
                return False
            elif you=='s':
                return True

        # checks possibilty of winning or losing 
        elif comp == 's':
            if you=='r':
                return False
            elif you=='p':
                return True


print('Computers turn to choose Rock(r) Paper(p) Sicissor(s)')
rand = random.randint(1,3)
if rand == 1:
    comp = 'r'
elif rand == 2:
    comp = 'p'
elif rand == 3:
    comp = 's'


you = input("Yours turn to Select Rock(r), Paper(p) ,Sicissor(s) \n")

a = gameWin(comp,you)

print(f'Computer chose {comp}')
print(f'you chose {you}')
if a==None:
    print('Game is a tie')
elif a:
    print('You have won')
else:
    print('You have lost') 