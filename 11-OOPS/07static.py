class Dogs:
    def myDog(self):
        print(f'Dog name is {self.name}')
        print(f'Dog fur present  {self.furs}')
        print(f'Dog gender is {self.gender}')
    
    @staticmethod
    def greetDog():
        print('good dog')

rancho = Dogs()
rancho.name = 'rancho'
rancho.breed = 'lab'
rancho.furs = 'yes'
rancho.legs = 4
rancho.gender = 'male'
rancho.food = 'drools'
rancho.myDog() # Dogs.myDog(rancho)
rancho.greetDog()
# by using self we can access the methods of attibutes and class 