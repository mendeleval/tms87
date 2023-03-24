# Дан список словарей. Каждый словарь описывает машину(серийный номер и год выпуска).
# Создать новый список со всеми машинами, год выпуска которых больше n

#
# dict = {key: value for value, key in enumerate(range(100, 110))}
# print(dict)

arr = [i for i in range(9)]
print(arr)
new_arr = [i * 2 for i in arr]
print(new_arr)
new_arr_2 = map(lambda x: x * 2, arr)
print(new_arr_2, type(new_arr_2))