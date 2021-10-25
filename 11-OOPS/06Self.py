class Dogs:
    def myDog(self):
        print(f'Dog name is {self.name}')
        print(f'Dog fur present  {self.furs}')
        print(f'Dog gender is {self.gender}')

rancho = Dogs()
rancho.name = 'rancho'
rancho.breed = 'lab'
rancho.furs = 'yes'
rancho.legs = 4
rancho.gender = 'male'
rancho.food = 'drools'
# rancho.myDog() # Dogs.myDog(rancho)

# by using self we can access the methods of attibutes and class 