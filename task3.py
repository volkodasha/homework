def my_func(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.remove(min(num1, num2, num3))
    print(f'Сумма двух наибольших чисел равна: {sum(numbers)}')


my_func(num1=int(input('Введите первое число: ')),
        num2=int(input('Введите второе число: ')),
        num3=int(input('Введите третье число: '))
        )
