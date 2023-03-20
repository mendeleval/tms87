# # Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент и поменять его местами
# # с элементом главной диагонали.
from random import randint

size_matrix = int(input('enter count str - '))
matrix = []
for i in range(size_matrix):
    column = []
    for j in range(size_matrix):
        column.append(randint(1, 9))
    matrix.append(column)
    print(column)

for index, number in enumerate(matrix):
    max_elem = max(number)
    index_max_elev = matrix.index(max_elem)
    matrix[index], matrix[index_max_elev] = matrix[index_max_elev], matrix[index]
