def calcPercent(student):
    percentage = ((student[0]+student[1]+student[2]+student[3])/400)*100
    return percentage

student1 = [22,10,78,99]
p1 = calcPercent(student1)
print(p1)


student2 = [99,99,99,99]
p2 = calcPercent(student2)
print(p2)