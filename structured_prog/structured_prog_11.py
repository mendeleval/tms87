# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1
#
# предоставить 2 решения. Одно с использованием цикла while, другое с использованием цикла for с параметром.
# Оба решения предоставить в одном файле.

my_list = [1, 2, 3, 4, 5, 6, 7]
my_list_new = []


while len(my_list) > 1:
    my_list_new.append(my_list.pop(1))

my_list_new.append((my_list.pop(0)))
print(my_list_new)

# for
my_list = [1, 2, 3, 4, 5, 6, 7]
my_list_new_2 = []

for i in range(1, len(my_list)):
    my_list_new_2.append(my_list[i])
my_list_new_2.append(my_list[0])
print(my_list_new_2)