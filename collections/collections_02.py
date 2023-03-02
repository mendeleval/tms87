# Создать список произвольного содержания. После каждой операции выводить список на экран
# Добавить к нему строку “Hello”.
# Удалить первый элемент.
# Поменять второй элемент на строку “World”.
# Удалить элемент “World”
# Вывести на экран перевернутый список

my_listt = [777, 888, 999]
print(my_listt)

my_listt.append('Hello')
print(my_listt)

my_listt.pop(0)
print(my_listt)

my_listt[1] = "world"
print(my_listt)

my_listt.remove("world")
print(my_listt)

my_listt.reverse()
print(my_listt)
