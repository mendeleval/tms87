# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы, которые кратны 3.

from random import randint

n = int(input('Размер матрицы: '))
sum_matrix = 0

matrix = []
for i in range(n):
    column = []
    for j in range(n):
        column.append(randint(1, 9))
    matrix.append(column)
    print(*column)
    for j in range(n):
        if j % 3 == 0:
            sum_matrix += j
print(matrix)
print(sum_matrix)