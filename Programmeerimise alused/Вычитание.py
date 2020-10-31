count = 0
uncount = 0
import random
while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print ('Сколько будет',a,'-', b)
    c = int(input())
    if c == a - b:
        print ('Отлично! Пример решён правильно!')
        count = count - 1
    while c != a - b:
        print ('Ответ решён не верно! Будьте внимательнее!')
        uncount = uncount - 1
        break