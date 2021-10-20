# 1. Create a class programmer for storing information 
# of few programmers working at microsoft

# class Employee:
#     company = "Microsoft"

#     def __init__(self, name, subunit, salary):
#         self.n = name
#         self.sub = subunit
#         self.sal = salary

#     def printInfo(self):
#         print(f'Company of the Employee is {self.company}')
#         print(f'Name of the Employee if {self.n}')
#         print(f'Subunit of the Employee if {self.sub}')
#         print(f'Salary of the Employee if {self.sal}')


# dia = Employee('Dia','Skype','50000')
# # dia.printInfo()

# tanu = Employee('Tanu','xbox','50000')
# tanu.company = 'Tencent'
# tanu.printInfo()

# Employee.company = 'Google'

# 5. Write a class Train which has methods to book a ticket
# get status(no of seats) and get fare 
# information of trains running under Indian Railways

class Railway:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def printInfo(self):
        print(f'Name of train is {self.name}')
        print(f'Fare of train is {self.fare}')
        print(f'Seats available of train is {self.seats}')

    def bookTicket(self):
        if(self.seats>0):
            print(f'Your ticket is booked and seat number is {self.seats}')
            self.seats = self.seats-1
        else:
            print('Sorry ticket not available try tatkal')

    def cancelTicket(self):
        pass

git = Railway("Gitanjali Express 12345",500,200)
git.printInfo()
git.bookTicket()
git.bookTicket()