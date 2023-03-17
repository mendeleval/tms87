# Составить список чисел Фибоначчи содержащий 15 элементов.
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны 1 и 1,
# а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
#
# предоставить 2 решения. Одно с использованием цикла while, другое с использованием цикла for с параметром.
# Оба решения предоставить в одном файле.


arr = [1, 1]
for i in range(13):
    arr.append(arr[-1] + arr[-2])
print(arr)

arr = [1 , 1]
while len(arr) < 15:
    arr.append(arr[-1] + arr[-2])
print(arr)