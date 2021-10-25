class Person:
    country = 'India'
    
    def singNationalAnthem(self):
        print('Person is singing national anthem')

class Employee(Person):
    company = 'Dell'

        
    def singNationalAnthem(self):
        print('Employee is singing national anthem')


class Programmer(Employee):

    company = "Twitter"

    def getSalary(self):
        print('there is no salary')
    
    def singNationalAnthem(self):
        print('Programmer is singing national anthem')


p = Programmer()
print(p.company)
print(p.country)
p.singNationalAnthem()
