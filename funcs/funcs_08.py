# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.

def average(*args):
    counter = 0
    for i in args:
        counter += i
    print(counter / len(args))


def geometric_mean(*args):
    counter = 1
    for i in args:
        counter *= i
    print(pow(counter, 1 / len(args)))


def type_ave(*args, mean_type):
    if mean_type == average:
        return (average(*args))
    elif mean_type == geometric_mean:
        return (geometric_mean(*args))


type_ave(2, 3, 2, 7, mean_type=average)
