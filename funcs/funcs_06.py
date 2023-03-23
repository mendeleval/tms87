# Создать функцию, которая принимает на вход неопределенное количество аргументов и возвращает их
# сумму и максимальное из них.

def my_func(*args):
    counter = 0
    max_arg = max(args)
    for arg in args:
        counter += arg
    print(f'sum - {counter}')
    print(f'max - {max_arg}')


my_func(1, 2, 3, 4)
