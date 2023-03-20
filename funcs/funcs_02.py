# Написать программу для работы с матрицами:
# Создание
# Вывод
# Сумма всех элементов
# Нахождение максимального элемента
# Нахождение минимального элемента.
from random import randint




def create_func():
    my_matrix = [[randint(1,9) for _ in range(4)]for _ in range(4)]
    print(my_matrix)
create_func()