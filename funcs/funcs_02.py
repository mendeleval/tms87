# Написать программу для работы с матрицами:
# Создание
# Вывод
# Сумма всех элементов
# Нахождение максимального элемента
# Нахождение минимального элемента.

from random import randint


def create_func():
    x = int(input('enter size - '))
    my_matrix = [[randint(1, 9) for _ in range(x)] for _ in range(x)]


# create_func()


