
from sys import argv
script_name, production, rate, prize = argv

def zp():
    try:
        wages = int(production) * int(rate) + int(prize)
    except:
        print('Ошибка ввода данных')
    else:
        wages = int(production) * int(rate) + int(prize)
        print('Заработная плата составила: ', wages)


zp()

