# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.
from random import randint

n = int(input('Размер матрицы: '))

matrix = []
# for i in range(n):
#     matrix.append([randint(1, 9)] * n)
# print(matrix)


for i in range(len(matrix)):
    for j in range(len([i])):
        ''' вместо новой строки печатаем пробел '''
        print(M[i][j], end=' ')
    ''' переход на новую строку после печати строки матрицы '''
    print()
