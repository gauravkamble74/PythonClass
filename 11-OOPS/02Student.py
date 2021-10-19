class Student:
    college = 'biyani college'
    def printInfo(self):
        print(f'Full name of student is {self.name}')
        print(f'Roll number is {self.roll_no}')
        print(f'cgpa is {self.cgpa}')
        print(f'college is {self.college}')

gaurav = Student()
gaurav.name = "Gaurav kamble"
gaurav.roll_no = 12
gaurav.address = 'Bhandara'
gaurav.cgpa = 8
gaurav.college = 'ram meghe'

gaurav.printInfo()

tanu = Student()
tanu.name = 'tanu sahu'
tanu.roll_no=1
tanu.cgpa = 8.5
tanu.printInfo()