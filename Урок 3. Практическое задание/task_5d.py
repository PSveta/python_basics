"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

number = int(input("Введите число: "))
my_list = [7, 5, 3, 3, 2]
for element in range(len(my_list)):
    if my_list[element] == number:
        my_list.insert(element + 1, number)
        break
    elif my_list[0] < number:
        my_list.insert(0, number)
    elif my_list[-1] > number:
        my_list.append(number)
    elif my_list[element] > number and my_list[element + 1] < number:
        my_list.insert(element + 1, number)
print(f"Пользователь ввел число {number}. Результат: {my_list}")