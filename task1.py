file_name = input('Название файла: ')
f = open(file_name,'w')
while True:
    text = input('Внесите информацию.\nДля окончания нажмите пробел и Enter.\n')
    if text == ' ':
        break
    f.write(text+'\n')

f.close()
