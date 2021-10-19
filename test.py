class Addition:
    print('i am inside class')

    def abc(self):
        return self.a + self.b;

x = Addition()
x.a = 4
x.b = 3
y = x.abc()
print(y)