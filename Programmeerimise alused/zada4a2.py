'''
2. ЗАДАЧА «ДРОБНАЯ ЧАСТЬ»
Дано положительное действительное число X. Выведите его дробную часть.
'''
chislo = float(input('Действительное число = '))
# Целая часть числа
a1 = int(chislo)
print ('1. Целая часть числа = ', a1)
a2 = chislo // 1
print ('2. Целая часть числа = ', a2)
b1 = chislo - a1
b2 = chislo - a2
print ('b1 = ',b1,'b2 = ',b2)
b3 = chislo % 1
print ('b3 = ',b3)
b4 = chislo % (int(chislo))
print ('b4 = ',b4)
