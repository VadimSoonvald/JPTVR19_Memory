class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Всего сотрудников:", Employee.empCount)
    def displayEmployee(self):
        print("Имя: ", self.name, ", Зарплата: ", self.salary)
print(Employee)
print(Employee.__doc__)
#Создание экземпляров объектов
emp1 = Employee("Andrey", 80000)
emp2 = Employee("Alex", 65000)
#Доступ к атрибутам
emp1.displayEmployee()
emp2.displayEmployee()
print("Всего сотрудников ", Employee.empCount)

emp1.age = 27
emp2.age = 35
#del emp1.salary Вы можете добавлять, удалять или изменять атрибуты классов и объектов в любое время

print("Имя: ", emp1.name, ", Возраст: ", emp1.age)
print("Имя: ", emp1.name, ", Зарплата: ", emp1.salary)

#ФУНКЦИИ АТРИБУТОВ И ВСТРОЕННЫЕ АТРИБУТЫ

print(hasattr(emp1, "salary"))
print(hasattr(emp1, "salary"))
setattr(emp1, "salary", 9000)
delattr(emp1, "salary")

#Встроенные атрибуты класса

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)