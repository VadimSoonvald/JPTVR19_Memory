'''
7. ЗАДАЧА «СУММА ЦИФР»
Дано трехзначное число. Найдите сумму его цифр.
'''
x = int(input('Трехзначное число = '))
x1 = x//100
x2 = (x//10)%10
x3 = x%10
print(x1) 
print(x2) 
print(x3) 
print(x1+x2+x3)
