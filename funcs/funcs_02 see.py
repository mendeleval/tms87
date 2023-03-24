# Написать программу для работы с матрицами:
# Создание
# Вывод
# Сумма всех элементов
# Нахождение максимального элемента
# Нахождение минимального элемента.

from random import randint


def create_matrix(n):
    arr = []
    for i in arr:
        arr_in = []
        for j in arr_in:
            arr.append(randint(0, 9))
        arr.append(arr_in)
    return arr


def print_matrix(arr):
    for num in arr:
        print(*arr)


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
    arr = create_matrix(5)
    print_matrix(arr)
    # print(sum_matrix(arr))
    # print(max_matrix(arr))
    # print(min_matrix(arr))
    #

if __name__ == "__main__":
    main()
