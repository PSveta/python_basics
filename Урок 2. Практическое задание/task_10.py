"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
N = int(input('Введите количество монет '))
orel = 0
reshka = 0
for i in range(N):
    x = int(input('Орел(1) или Pешка(0)? '))
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f'Переверните {orel} монет с орла на решку, их меньше всего')
else:
    print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))

