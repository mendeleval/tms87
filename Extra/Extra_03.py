# Есть список arr = [1,2,3,4,4,4,5,5,2]
# Найти среднее геомнтрическое

arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
multiply_values = 1 * 2 * 3 * 4 * 4 * 4 * 5 * 5 * 2
n = 9
geometric = multiply_values ** (1 / n)
print(str(geometric))
