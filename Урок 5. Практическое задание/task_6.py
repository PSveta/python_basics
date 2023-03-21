"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random

rand = random.randint(0, 100)


def guess_num(n, rand, i):
    rand = int(input('Введите число\n'))
    if rand == n:
        return print(f'Верно! Вы угадали число!')
    elif i == 10:
        x = input('Вы исчерпали свои 10 попыток: ')
        if x == 'y':
            rand_init = random.randint(1, 100)
            guess_num(rand_init, 0, 1)
        else:
            return
    elif rand > n:
        print('Загаданное число меньше', '\n')
        guess_num(n, rand, i + 1)
    elif rand < n:
        print('Загаданное число больше', '\n')
        guess_num(n, rand, i + 1)

guess_num(rand, 0, 1)
