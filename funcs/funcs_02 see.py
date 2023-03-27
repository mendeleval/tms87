# Написать программу для работы с матрицами:
# Создание
# Вывод
# Сумма всех элементов
# Нахождение максимального элемента
# Нахождение минимального элемента.

from random import randint


def create_matrix(n):
    arr = []
    for i in range(n):
        column = []
        for j in range(n):
            column.append(randint(1, 9))
        arr.append(column)
    return arr


def print_matrix(arr):
    for num in arr:
        print(arr)


# def sum_matrix(arr: list) -> int:
#     summ = 0
#     for i in arr:
#         for j in i:
#             summ += j
#     return summ
#
#
# def max_matrix(arr):
#     return max([max(arr) for i in arr])
#
#
# def min_matrix(arr):
#     return min([min(arr) for i in arr])


def main():
    create_matrix(4)
    print_matrix()
    # print(sum_matrix(arr))
    # print(max_matrix(arr))
    # print(min_matrix(arr))
    #


if __name__ == "__main__":
    main()
