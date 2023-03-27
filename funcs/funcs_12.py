# Дан массив целых чисел A. Найти суммы положительных и отрицательных элементов массива,
# используя функцию определения суммы


def my_func(*args):
    positive = []
    negative = []
    for i in args:
        if i > 0:
            positive.append(i)
        else:
            negative.append(i)
    print(f'sum positive : {sum(positive)} \nsum negative : {sum(negative)}')


my_func(1, 3, 4, -2, -7, -10, 4, 3)
