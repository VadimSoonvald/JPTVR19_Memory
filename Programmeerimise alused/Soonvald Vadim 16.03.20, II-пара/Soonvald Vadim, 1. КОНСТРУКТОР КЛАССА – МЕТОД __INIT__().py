class Person:
    def setName(self,n,s):
        self.name = n
        self.surname = s
p1 = Person()
p1.setName("Bill", "Ross")
print(p1.name, p1.surname)

class Person:
    def __init__(self, n, s):
        self.name = n
        self.surname = s
p1 = Person("Sam", "Baker")
print(p1.name, p1.surname)

#p2 = Person()

class Rectangle:
    def __init__(self, w = 0.5, h = 1):
        self.width = w
        self.height = h
    def square(self):
        return self.width * self.height
    
rec1 = Rectangle(5, 2)
rec2 = Rectangle()
rec3 = Rectangle(3)
rec4 = Rectangle(h = 4)

print('1 -', rec1.square(),rec1.height,rec1.width)
print('2 -', rec2.square(),rec2.height,rec2.width)
print('3 -', rec3.square(),rec3.height,rec3.width)
print('4 -', rec4.square(),rec4.height,rec4.width)
