from datetime import datetime
import random

def goroda():

    """Включает игру города"""
    
    letter = 'А'
    first = ''
    second = ''
    used_words = []

    print('Если захотите выйти, введите СТОП')

    while True:
        while first != letter or first != 'СТОП':
            first = input(f'Введите слово на букву {letter}, первый игрок: ')
            if first == 'СТОП':
                return 0
            elif first in used_words:
                print('Было')
            elif len(first) >= 2 and first[0] == letter:
                used_words.append(first)
                break
        if first[-1] == 'ь':
            letter = first[-2].capitalizze()
        else:
            letter = first[-1].capitalize()
        print('Хорошо')

        while True:
            second = input(f'Введите слово на букву {letter}, второй игрок: ')
            if second == 'СТОП':
                return 0
            elif second in used_words:
                print('Было')
            elif len(second) >= 2 and second[0] == letter:
                used_words.append(second)
                break
        if first[-1] == 'ь':
            letter = second[-2].capitalize()
        else:
            letter = second[-1].capitalize()
        print('Хорошо')


def reakcia_test():

    """

    Запускает тест на реакцию, где вы должны быстро ввести цифру

    """
    
    answer = ''
    times = []
    number = random.randint(0, 9)
    for i in range(5):
        print(number)
        start_time = datetime.now()
        start_time = start_time.minute * 60 + start_time.second
        while answer != number:
            answer = int(input('Введите это число: '))
        if answer == number:
            finish_time = datetime.now()
            finish_time = finish_time.minute * 60 + finish_time.second
            answer_time = finish_time - start_time
            times.append(answer_time)
            number = random.randint(0, 9)
            print('Дальше')

    middle_time = sum(times) / len(times)
    print(f'Среднее время ответа: {middle_time} секунд')

def random_number_game():

    """

    Запускает игру, где вы должны угадать число загаданное

    """
    
    try:
        d_l = input('Выберите уровень сложности (1 - легкий, 2 - нормальный, 3 - СЛОЖНЫЙ): ')
        dls = ['1', '2', '3']
        if d_l not in dls:
            print('Некорректный ввод')
            return
        if d_l == '1':
            a, b = 0, 5
        elif d_l == '2':
            a, b = 0, 10
        elif d_l == '3':
            a, b = 0, 20
    except:
        print('Ошибка ввода')
        return

    print('Игра началась')
    number = random.randint(a, b)
    task = None

    while task != number:
        try:
            task = int(input('Введите число от {} до {}: '.format(a, b)))
        except ValueError:
            print('Некорректный ввод')
            continue

        if task == -1:
            print('Выход из игры')
            return

        if task < a or task > b:
            print('Число должно быть от {} до {}: '.format(a, b))
        elif task > number:
            print('Меньше')
        elif task < number:
            print('Больше')
        else:
            print('Ты угадал!')

def quickly_calculate():

    """

    Запускает игру, где вы должны быстро посчитать пример
    
    """
    
    answer = ''
    args = ['+', '-']
    times = []
    first, to = 0, 9

    for i in range(5):
        arg = random.choice(args)
        if arg == '+':
            n1 = random.randint(first, to)
            n2 = random.randint(first, to)

            right_answer = n1 + n2

            start_time = datetime.now()
            start_time = start_time.minute * 60 + start_time.second
            
            while answer != right_answer:
                try:
                    answer = int(input(f'{n1} + {n2} = '))
                except:
                    ValueError
                if answer == right_answer:
                    finish_time = datetime.now()
                    finish_time = finish_time.minute * 60 + finish_time.second
                    answer_time = finish_time - start_time
                    times.append(answer_time)
                    print('Правильно!')
                    break
        
        elif arg == '-':
            n1 = random.randint(first, to)
            n2 = random.randint(first, to)

            right_answer = n1 - n2
            
            start_time = datetime.now()
            start_time = start_time.minute * 60 + start_time.second

            while answer !=  right_answer:
                try:
                    answer = int(input(f'{n1} - {n2} = '))
                except:
                    ValueError
                    print('ВВЕДИТЕ ЦИФРЫ!')
                if answer == right_answer:
                    finish_time = datetime.now()
                    finish_time = finish_time.minute * 60 + finish_time.second
                    answer_time = finish_time - start_time
                    times.append(answer_time)
                    print('Правильно!')
                    break

    middle_time = sum(times) / len(times)
    print(f'Среднее время ответа: {middle_time} секунд')
