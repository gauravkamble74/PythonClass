class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2):
        print("Addition time")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Multiplication time")
        return self.num * num2.num

obj1 = Number(9)
obj2 = Number(4)

add = obj1 + obj2
mul = obj1 * obj2

print(add)
print(mul)
