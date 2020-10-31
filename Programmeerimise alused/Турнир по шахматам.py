import random
print('Добро пожаловать на турнир по шахматам')
a = 'Антон Андрей Евгений Артём Давид Лев Александр Михаил Оксана Валерия Олеся Алеся Наталия Антонина Карина Алиса Ксения София  Мария  Анна  Алиса  Виктория Анастасия  Полина  Александра  Елизавета  Екатерина Антон Андрей Евгений Артём Лев Марк Александр Михаил Дмитрий Матвей Даниил Сергей Максим Владимир Ярослав Владислав Глеб Демид Мирон Виктор Степан Богдан Тимофей Фёдор'
imena = a.split()
#print(imena)
reg = []
for i in range(30):
    v = random.randint(8,15)
    n = imena[random.randint(0,50)]
    reg.append([n,v])
    print(reg[i])
vozrast = []
for i in range(30):
    vozrast.append(reg[i][1])
print(vozrast)

vozrast.sort()
print(vozrast)

vozrast.reverse()
print(vozrast)
mas1 = set(vozrast)
print(mas1)

mas_count = []
for i in mas1:
    print(i, vozrast.count(i))
    mas_count.append([i, vozrast.count(i)])
    
print(mas_count)
n = len(mas_count)

#factorial (сколько участника съиграют игр)