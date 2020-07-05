def my_func(x, y):
    result = 1 / x ** abs(y)
    print(result)


my_func(x = int(input('Введите целое положительное число: ')),
        y = int(input('Введите целое отрицательное число: ')))