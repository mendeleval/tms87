# Создать функцию, которая принимает на вход неопределенное количество именованных аргументов
# и выводит на экран те из них, длина ключа которых четна.


def my_func(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 != 0:
            print(kwargs[key])


my_func(key97=97, key777=777, key12=12, key654=654)
