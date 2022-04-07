#нахождение минимального из 3-х чисел
a=input('Введите целое число \n')
b=input('Введите целое число \n')
c=input('Введите целое число \n')
if a<b:
    if a<c:
        y=a
    else:
            y=c
else:
    if b<c:
        y=b
    else:
        y=c
        print('минимальное:',y)
    
