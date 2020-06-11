start = int(input('Дистанция в первый день, км: '))
end = int(input('Дистанция конечная, км: '))

day=1
while end - start > 0:
    start = start + start*0.1
    day = day + 1

print(f'Чтобы пробежать {end} км, потребуется {day} дней')