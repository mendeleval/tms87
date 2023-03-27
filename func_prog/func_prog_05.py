# Дан список чисел. Вернуть список, где каждое число переведено в строку
# [5, 3] -> [‘5’, ‘3’]

my_list = [5, 7, 8, 9]
new_list = []
for elem in my_list:
    new_elem = str(elem)
    new_list.append(new_elem)
print(new_list)
