class Person:
    name=""
    money = 0
bob = Person()
bob.name = "Bob"
bob.money = 100

nancy = bob
nancy.name = "Nancy"
print(bob.name,"has",bob.money,"dollars.")
print(nancy.name,"has",nancy.money,"dollars.")

#ФУНКЦИИ И ССЫЛКИ

def giveMoney1(money):
    money += 100
class Person:
    name = ""
    money = 0
bob = Person()
bob.name = "Bob"
bob.money = 100

giveMoney1(bob.money)
print(bob.money)

def giveMoney2(person):
    person.money += 100

giveMoney2(bob)
print(bob.money)