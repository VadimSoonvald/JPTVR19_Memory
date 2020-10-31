import datetime
date = datetime.date.today()
print(60*'=')
print('Работу выполнил: Vadim Soonvald')
print('Группа: JPTVR19')
print(60*'=')
while True:
    isikukood = input('Введите ваш isikukood:') #Контроль вводимых символов
    a = len(isikukood)
    if a != 11:
        print('Вы ввели неправильный isikukood')
        continue
    else:
        print('Вы ввели правильный isikukood')
    break
b = list(isikukood)
print(60*'=')
#print(b)
#print(60*'=')
c = isikukood[0]
if c == '0':
    print('Вы допустили ошибку в написании первой цифры, программа не смогла определить пол') #Проверка на пол 
if c == '1':
    print('Вы допустили ошибку в написании первой цифры, программа не смогла определить пол') #Проверка на пол
if c == '2':
    print('Вы допустили ошибку в написании первой цифры, программа не смогла определить пол') #Проверка на пол
if c == '3':
    print('Ваш пол: мужчина') #Проверка на пол
if c == '4':
    print('Ваш пол: женщина') #Проверка на пол
if c == '5':
    print('Ваш пол: мужчина') #Проверка на пол
if c == '6':
    print('Ваш пол: женщина') #Проверка на пол
if c == '7':
    print('Вы допустили ошибку в написании первой цифры, программа не смогла определить пол') #Проверка на пол
if c == '8':
    print('Вы допустили ошибку в написании первой цифры, программа не смогла определить пол') #Проверка на пол
if c == '9':
    print('Вы допустили ошибку в написании первой цифры, программа не смогла определить пол') #Проверка на пол

god = isikukood[1:3] #Вывод даты рождения
if god >= '00' and god <= '99' and c == '3':
    print('Дата вашего рождения:',isikukood[5:7]+'.'+isikukood[3:5]+'.19'+ god)
if god >= '00' and god <= '99' and c == '5':
    print('Дата вашего рождения:',isikukood[5:7]+'.'+isikukood[3:5]+'.20'+ god)
if god >= '00' and god <= '99' and c == '4':
    print('Дата вашего рождения:',isikukood[5:7]+'.'+isikukood[3:5]+'.19'+ god)
if god >= '00' and god <= '99' and c == '6':
    print('Дата вашего рождения:',isikukood[5:7]+'.'+isikukood[3:5]+'.20'+ god)


voz = date.year #Вывод возраста
if date.month > int(isikukood[5:7]) and c in ('5','6'):
    print('Сейчас вам:',voz - int('20' + isikukood[1:3]) + 1)
if date.month < int(isikukood[5:7]) and c in ('5','6'):
    print('Сейчас вам:',voz - int('20' + isikukood[1:3]) - 1)
if date.month > int(isikukood[5:7]) and c in ('3','4'):
    print('Сейчас вам:',voz - int('19' + isikukood[1:3]) + 1)
if date.month < int(isikukood[5:7]) and c in ('3','4'):
    print('Сейчас вам:',voz - int('19' + isikukood[1:3]) - 1)
print(60*'=')