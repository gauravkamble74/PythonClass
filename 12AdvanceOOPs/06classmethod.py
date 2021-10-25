class Employee:
    company = 'facebook'
    salary = 1000

    # def changeSalary(self , sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls , sal):
        cls.salary = sal

    def printSalary(self):
        print(f'salary is {self.salary}')

obj = Employee()
# obj.printSalary()
obj.changeSalary(2000)
print(obj.salary)
print(Employee.salary)