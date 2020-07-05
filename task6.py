word = input('Введите слово: ')

def int_func(word):
    return word.capitalize()


print(int_func(word))


my_str = input('Введите строку: ')
new_str = my_str.split(' ')
new_str_big = list(map(int_func, new_str))

print(' '.join(new_str_big))
