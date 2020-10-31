import random #Импортирую рандом
import datetime #Импротирую время

#Информация об авторе работы
print(100*'=')
print('Тема работы: Работа с текстовыми файлами, а также создание и обработка словарей.')
now_date = datetime.date.today ()
print('Дата: ', now_date)
print(100*'=')
print('Автор работы: Vadim Soonvald')
print('Специальность: Tarkvaraarendaja')
print('Группа: JPTVR19')
print(100*'=')
print("Добро пожаловать в программу, где Вы сможете дополнять словарь, искать нужные вам слова, а также пройти тест на знание слов из словаря.")
print("На данный момент в словаре находятся данные слова:")

#Чтение русского и английского словаря
file = open("dictionary1.txt") #Русский словарь
file1 = open("dictionary2.txt") #Английский словарь
dictionary = file.readlines() #Русский словарь
dictionary1 = file1.readlines() #Английский словарь
file.close() #Русский словарь
file1.close() #Английский словарь
#print(dictionary) #Русский словарь
#print(dictionary1) #Английский словарь
len_dictionary = len(dictionary) #Русский словарь
len_dictionary1 = len(dictionary1) #Английский словарь
#print(len_dictionary) #Русский словарь
#print(len_dictionary1) #Английский словарь
key,value = dictionary[0].split() #Русский словарь
key1,value1 = dictionary1[0].split() #Английский словарь
#print(key,value) #Русский словарь
#print(key1,value1) #Английский словарь
mydict = dict() #Русский словарь
mydict1 = dict() #Английский словарь
#print(mydict) #Русский словарь
#print(mydict1) #Английский словарь

#Запись новых слов в словарь (как в русский словарь, так и в английский)
for i in range(len(dictionary)):
    key,value = dictionary[i].split()
    mydict[key] = value
print(mydict)
for j in range(len(dictionary1)):
    key1,value1 = dictionary1[j].split()
    mydict1[key1] = value1
print(mydict1)
while True:
    a = input("Введите слово для поиска в словаре: ") #Поиск слова в словаре
    if a in mydict:
        print("Данное слово есть в словаре,","это слово",a,",его перевод",mydict[a]) #Поиск слова в словаре
    else:
        if a in mydict1:
            print("Данное слово есть в словаре,","это слово",a,",его перевод",mydict1[a]) #Поиск слова в словаре
        else:
            print("Данного слова нету в словаре.") #Поиск слова в словаре
            answer = input("Желаете ввести слово? Если да, то введите yes, если нет, то введите no: ") #Добавление нового слова в словарь (как в русский словарь, так и в английский)
            if answer == "yes":
                print(100*'=')
                key,value = input("Введите слово на английском и через пробел на русском языке: ").split()
                value1,key1 = value,key
                #print(key,value)
                #print(value1,key1)
                mydict[key] = value
                mydict1[value1] = key1
                #print(mydict)
                #print(mydict1)
                print("Ваше слово успешно было добавленно в словарь!")
                print(100*'=')
            if answer == "no":
                break

#Запись словаря в текстовый документ (как в русский документ, так и в английский)
print("="*50)
print("Сохранение словаря...")
f = open("dictionary1.txt", "w") #Открытие русского словаря (текстовый документ)
f1 = open("dictionary2.txt", "w") #Открытие английского словаря (текстовый документ)
for word in mydict:
    key = word
    value = mydict[key]
    f.write(key + " " + value + "\n") #Запись в русский словарь (текстовый документ)
for word1 in mydict1:
    key1 = word1
    value1 = mydict1[key1]
    f1.write(key1 + " " + value1 + "\n") #Запись в английский словарь (текстовый документ)
f.close()
f1.close()
print("Сохранение словаря прошло успешно!")
print("="*50)

#Тест для проверки знаний слов из словаря
#Проверка с английского на русский
while True:
    answer = input("Вы желате пройти тест на проверку знаний слов из словаря? Если да, то введите yes, если нет, то введите no: ")
    if answer == "yes":
        answer = input("Выбирите задание, с какого на какой язык вы хотите тренироваться, если с русского на английский, то введите eng, если с английского на русский, то введите rus: ")
        if answer == "rus":
            file = open("dictionary1.txt")
            eng_words = []
            dictionary={}
            for row in file.readlines():
                eng, rus = row.strip().split()
                dictionary[eng] = rus
                eng_words.append(eng)
            random.shuffle(eng_words)
            file.close()
            count = 0
            n = int(input("Сколько слов Вы хотите перевести?\nНо, Вы не можете выбрать больше слов, чем их находится в словаре: "))
            for word in eng_words[:n]:
                guess = input(f'Как Вы переведете слово {word}? ')
                if guess.strip() == dictionary[word]:
                    print("Вы правильно перевели слово! Вы большой молодец! ")
                    count+=1
                else:
                    print("Вы неправильно перевели слово! Стоит его запомнить, чтобы не ошибиться в следующий раз! ")
            print("="*50)
            print("Результаты теста...")
            print("Вы правильно перевели",count,"из",n,"слов.")
            print("="*50)
            answer = input("Желаете пройти тест ещё раз? Если да, то введите yes, если нет, то введите no: ")
            if answer == "yes":
                continue
            else:
                print("Спасибо за проведенное время в моей программе! До новых встреч!")
                break
    if answer == "no":
        print("Спасибо за проведенное время в моей программе! До новых встреч!")
        break

#Проверка с русского на английский
    else:
        if answer == "eng":
            file = open("dictionary2.txt")
            rus_words = []
            dictionary={}
            for row in file.readlines():
                rus, eng = row.strip().split()
                dictionary[rus] = eng
                rus_words.append(rus)
            random.shuffle(rus_words)
            file.close()
            count = 0
            n = int(input("Сколько слов Вы хотите перевести?\nНо, Вы не можете выбрать больше слов, чем их находится в словаре: "))
            for word in rus_words[:n]:
                guess = input(f'Как Вы переведете слово {word}? ')
                if guess.strip() == dictionary[word]:
                    print("Вы правильно перевели слово! Вы большой молодец! ")
                    count+=1
                else:
                    print("Вы неправильно перевели слово! Стоит его запомнить, чтобы не ошибиться в следующий раз! ")
            print("="*50)
            print("Результаты теста...")
            print("Вы правильно перевели",count,"из",n,"слов.")
            print("="*50)
            answer = input("Желаете пройти тест ещё раз? Если да, то введите yes, если нет, то введите no: ")
            if answer == "yes":
                continue
            else:
                print("Спасибо за проведенное время в моей программе! До новых встреч!")
                break
    if answer == "no":
        print("Спасибо за проведенное время в моей программе! До новых встреч!")
        break
    
#Задание было выполнено с душой и любовью, прошу строго не судить, я старался. - Вадим