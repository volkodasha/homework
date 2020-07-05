def div(number1, number2):
    try:
        result = number1 / number2
    except ZeroDivisionError:
        print('На 0 делить нельзя!')
    else:
        print(f'Результат деления: %.3f' % result)


div(number1=int(input('Введите первое число: ')), number2=int(input('Введите второе число, не равное 0: ')))
