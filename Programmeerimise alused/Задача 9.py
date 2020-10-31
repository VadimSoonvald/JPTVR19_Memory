'''
9. ЗАДАЧА «КОЛИЧЕСТВО НУЛЕЙ»
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Для ввода данных
предложите цикл – выход из цикла ввод пустой строки (нажатие ENTER).
Подсчитайте количество нулей среди введенных чисел и выведите это количество
'''
sum_ = 0
n = int(input('n='))
count_0 = 0
for i in range(1, n+1):
    print (str(i) + '.','Ваше число = ', end = ' ')
    chislo = input()
    if chislo == '' or (not chislo.isdigit() ):
        break
    chislo = int(chislo)
    if chislo == 0:
        count_0 = count_0 + 1
    sum_ = sum_ + chislo
print('\nКонец цикла')
print('count_0', count_0, 'sum = ', sum_)