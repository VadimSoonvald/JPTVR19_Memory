'''
5. ЗАДАЧА «БАНКОВСКИЕ ПРОЦЕНТЫ»
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего
дробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее y
рублей.
Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567
рублей, т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек,
т.е. 123.45 рублей.
Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
'''
vklad = int(input('Вклад ='))
p = int(input('Процент ='))
summa = int(input('Желаемая сумма ='))
let = 0
while vklad < summa:
    vklad = vklad + vklad * p/100
    print (let, vklad)
print ('let = ',let)