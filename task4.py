#Вижу, что очень кривое решение. Но не смогла сгенерировать ничего лучше. При вводе отрицательного числа криво раюотает,
#поэтому не стала писать в else.

num = int(input('Введите любое положительное число: '))
max = num%10
num = num//10

while num > 0:
    if max == 9:
        break
    elif max == 8:
        break
    elif max == 7:
        break
    elif max == 6:
        break
    elif max == 5:
        break
    elif max == 4:
        break
    elif max == 3:
        break
    elif max == 2:
        break
    elif max == 1:
        break

print(f'Наибольшая цифра в числе: {max}')