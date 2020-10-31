a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > b:
    if a > c:
        m = a
    else:
        m = c
    
else:
    if b > c:
        m = b
    else:
        m = c
print('m =',m)

    