class Engineering:
    university = "Sant Gadge Baba"

    def showPassStats(self):
        print('only 50% passed')

class CSE(Engineering):
    def __init__(self, name , rollno):
        self.name = name
        self.rollno = rollno

    def showDetails(self):
        print("Name of student is ",self.name)
        print('Roll no of student is ',self.rollno)

    # def showPassStats(self):
    #     print('only 1000% passed of cse branch')


obj = CSE("Gaurav","17")
obj.showDetails()
# obj.showPassStats()
# print(obj.name)
print(obj.university)
# obj.showPassStats()