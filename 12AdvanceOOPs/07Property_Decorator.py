class Employee:
    company = "microsoft"
    salary = 1000
    salarybonus = 500
    # totalSalary = 1500

    # this is getter 
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    # this is setter 
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
# print(e.salary)

# x = e.totalSalary()
# print(x)

print(e.totalSalary)
e.totalSalary = 5000
print(e.salary)
print(e.salarybonus)
# print(e.totalSalary)
