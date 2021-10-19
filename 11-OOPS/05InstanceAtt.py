class Student:
    # below line is class attribute 
    college = 'biyani college'
    def printInfo(self):
        print(f'Full name of student is {self.name}')
        print(f'Roll number is {self.roll_no}')
        print(f'cgpa is {self.cgpa}')
        print(f'college is {self.college}')

gaurav = Student()
# below is instance attribute
# preference of instance class is more over class attributes 
gaurav.name = "Gaurav kamble"
gaurav.roll_no = 12
gaurav.address = 'Bhandara'
gaurav.cgpa = 8
# we can explictily change value of college 
gaurav.college = 'ram meghe'
gaurav.printInfo()
