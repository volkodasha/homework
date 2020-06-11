time = int(input('Введите число секунд: '))
hours = time // 3600
min = (time % 3600) // 60
sec = (time % 3600) % 60

result = (f'Время: {hours:02}:{min:02}:{sec:02}')
print(result)