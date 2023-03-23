# Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать функцию.
# Подсказка: для хранения данных использовать словарь.
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in
from random import randint
my_list = [4, 5, 6, 7, 3, 34, 55, 4, 55, 7, 4, 4, 3, 7, 4, 4]


# def my_func(arr):
#     my_dict = {}
#     for i in set(arr):
#         my_dict[i] = arr.count(i)
#     return dict


def counter_numbers_in_list_2(arr):
    my_dict = {}
    for i in arr:
        if my_dict.get(i):
            my_dict[i] = my_dict + 1
        else:
            my_dict[i] = 1
    return my_dict


def main():
