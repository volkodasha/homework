from itertools import count, cycle

for el in count(3):
    print(el)
    if el == 10:
        break


numbers = ['три', 'два', 'один']
score = 0
for i in cycle(numbers):
    if score != 5:
        print(numbers)
        score += 1