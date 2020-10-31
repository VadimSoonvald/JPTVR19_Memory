import datetime
from random import randint
import random
 
print(100*'=')
print('Тема работы: Диктант.')
now_date = datetime.date.today ()
print('Дата: ', now_date)
print(100*'=')
print('Автор работы: Vadim Soonvald')
print('Специальность: Tarkvaraarendaja')
print('Группа: JPTVR19')
print(100*'=')
 
#1
a = random.randint(10,20)
b = random.randint(10,20)
print(a,b)
 
#2
c = a//b
c1 = a%b
print(c,c1)
 
#3
if a%5==0:
    print('yes')
else:
    print('no')
if a > b:
    e=a-b
    print(e)
if a < b:
    e=b-a
    print(e)
 
#4
a1 = 'school'
a1.lower()
print(a1)
print(a1[1],a1[5])
 
#5
if "a" in a1:
    print("Да, это буква есть")
    a1.index("a")
else:
    print('Данной буквы нет')
 
#6
for i in a1:
    print(i)
 
#7
g = 1
while g!=6:
    u = random.randrange(0,30)
    print(str(g)+". ",u)
    g+=1
   
#8
r1 = []
r1.append(random.randrange(0,30))
r1.append(random.randrange(0,30))
r1.append(random.randrange(0,30))
r1.append(random.randrange(0,30))
r1.append(random.randrange(0,30))
print(r1)
 
#108 Альтернативный способ решения задачи №8 (более правильный в исполнении)
r2 = []
for h in range(5):
    appnd_number = random.randint(0, 30)
    r2.append(appnd_number)
print(r2)
 
#9
xy=[]
x=[]
y=[]
for i in range(5):
    X = random.randrange(-10,10)
    Y = random.randrange(-10,10)
    x.append(X)
    y.append(Y)
    xy.append(X)
    xy.append(Y)
print(xy)
 
#109 Альтернативный, а также правильный способ решения задачи №9 (работа с двумерным массивом)
n = 2 #Количество строк (то же самое как x,y из предыдущего задания)
m = 5 #Сколько будет сгенерировано цифр
a = [[randint(-10, 10) for j in range(m)] for i in range(n)] #использовал randint, так как в начале из from random вытайщил import randint, чтобы показать разновидности решения  
print(a)
 
#10
s1 = dict()
s1["Russia"] = "Moskow"
s1["Eesti"] = "Tallinn"
s1["Ukraine"] = "Kiev"
print("Кол-во слов: ",len(s1))
print(s1)
as1 = "мир"
if as1 in s1:
    print("Данное слово есть в словаре.")
else:
    print("Данного слова нету в словаре.")
 
#11
file = open("filezapisi.txt", "w")
for i in range(2):
    for j in range(5):
        d = file.write(str(a[i][j])) #Не смог добавить пробел, так как выдает ошибку, где написано, что можно использовать только str

for word in s1:
    key = word
    value = s1[key]
    file.write("\n"+ key + " " + value + "\n")
file.close()
 
#12
#x = input("1 значение: ")
#y = input("2 значение: ")
 
#112 Имеется 4 четверти. По введенному x и y нужно определить какая четверть.
x = input("1 значение: ")
y = input("2 значение: ")
if x >= '0' and y >= '0':
    print("Относится к первой четверти")
if x <= '0' and y >= '0':
    print("Относится к второй четверти")
if x <= '0' and y <= '0':
    print("Относится к третьей четверти")
if x >= '0' and y <= '0':
    print("Относится к четвёртой четверти")