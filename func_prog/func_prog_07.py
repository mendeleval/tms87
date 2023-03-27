# Дан список чисел. Найти произведение всех чисел, которые кратны 3.

arr = [3, 15, 10, 5, 7, 12]
new_arr = list(filter(lambda x: x % 3 == 0, arr))
result = 1
for i in new_arr:
    result *= i

print(f'Кратные 3м - {new_arr}')
print(f'Произведение - {result}')