from datetime import datetime
import time
from pynput import keyboard

def time_now():
    time = datetime.now()
    print(f'Время сейчас: {time}')

def timer():
    time_wait = input('Введите время, которое вы хотите засечь(часы, минуты, секунды) через пробел ЦИФРАМИ:').split()
    times = list(map(int, time_wait))
    timer = times[0] * 3600 + times[1] * 60 + times[2]

    print('Начало')
    
    a = 1
    for i in range(timer):
        time.sleep(1)
        print(f'Прошло {a} сек.')
        a += 1

    print('Время вышло!')

timer()