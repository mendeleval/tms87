# Создать функцию, принимающая на вход неопределенное количество аргументом и возвращающая сумму args[i] * i
# Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10

def my_args(*args):
    counter = 0
    args_counter = 0
    for i in args:
        args_counter += i * counter
        counter += 1
    print(args_counter)


my_args(4, 3, 2, 1)