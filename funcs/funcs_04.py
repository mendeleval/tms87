# Реализовать функцию возвращающую матрицу. На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9))

from random import randint


def matrix(n, random_from=1, random_to=9):
    my_matrix = [[randint(random_from, random_to) for _ in range(n)] for _ in range(n)]
    print(my_matrix)


matrix(4)
