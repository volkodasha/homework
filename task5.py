revenue = int(input('Введите вашу выручку: '))
cost = int(input('Введите Ваши издержки: '))

if revenue < cost:
    print('Ваша фирма работает в убыток')
elif revenue == cost:
    print('Вы работаете в ноль. Выручка равна издержкам.')
elif revenue > cost:
    profit = revenue - cost
    profitability = profit/revenue
    print(f'Ваша фирма получает прибыль {profit}. Рентабельность выручки составляет %.2f' % profitability)
    person = int(input('Введите число сотрудников: '))
    if person > 0:
        profit_per_person = profit / person
        print(f'Прибыль на каждого сотрудника составляет {profit_per_person}')
    else:
        print ('Вы ввели некорректное число')

else:
    print('Вы ввели некорректные данные')
