print('Здравствуйте! Вас приветствует ассистент Неии!')
def registration():
    name = input('Введите ваше имя: ').capitalize()
    flag = False
    while flag != True:
        age = input('Введите ваш возраст: ')
        try:
            age = int(age)
            if age < 18:
                print('Ты еще маленький! Нельзя!')
                flag = True
                return 'Пока!'
            else:
                if age < 80:
                    print('Хорошо')
                    flag = True
                else:
                    print('Да вы долгожитель!')
                    flag = True
        
        except:
            TypeError
            print('Введите ЦИФРЫ')
            flag = False
        
    print(f'Добро пожаловать, {name}!')