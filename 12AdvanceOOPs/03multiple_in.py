class Freelancer:
    level = 0
    company = "Fiverr"

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Google"
    salary = 1000

class Programmer(Freelancer, Employee):
    def printSalaryInfo(self):
        print(f'no salary')

p = Programmer()
# p.printSalaryInfo()
print(p.level)
p.upgradeLevel()
print(p.level)