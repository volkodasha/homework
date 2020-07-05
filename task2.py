def form(**kwargs):
    return kwargs.values()



def form_2():
    input(form(name=input('Имя: '),
               surname=input('Фамилия: '),
               city=input('Город: '),
               email=input('email: '),
               tel=input('Телефон: ')))


form_2()
