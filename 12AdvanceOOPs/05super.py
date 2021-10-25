class Person:
    country = 'India'
    
    def __init__(self):
        print('Person Initialized')

    def singNationalAnthem(self):
        print('Person is singing national anthem')

class Employee(Person):
    company = 'Dell'

    def __init__(self):
        super().__init__()
        print('Employee Initialised')
        
    def singNationalAnthem(self):
        super().singNationalAnthem()
        print('Employee is singing national anthem')


class Programmer(Employee):

    company = "Twitter"

    def __init__(self):
        super().__init__()
        print('Programmer initialized')

    def getSalary(self):
        print('there is no salary')
    
    def singNationalAnthem(self):
        super().singNationalAnthem()
        print('Programmer is singing national anthem')


p = Programmer()
# print(p.company)
# print(p.country)
p.singNationalAnthem()
