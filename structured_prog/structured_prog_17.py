# В массиве целых чисел с количеством элементов 19 определить максимальное число
# и заменить им все четные по значению элементы.

my_list = [1, 2, 3, 4, 70, 6, 15, 20, 66, 76, 87, 75, 80, 77, 12, 11, 100, 64, 13]
max_number = []

swapped = True
while swapped:
    swapped = False
    for i in my_list:
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            swapped = True

print(my_list)