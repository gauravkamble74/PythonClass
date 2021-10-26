class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2):
        print("Addition time")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Multiplication time")
        return self.num * num2.num
    
    def __len__(self):
        return 1
    
    def __str__(self):
        return f"Decimal Number : {self.num}"

obj1 = Number(9)
obj2 = Number(4)

# print(len(obj1))

# print(obj1)