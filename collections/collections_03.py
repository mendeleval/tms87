# Создать список произвольного содержания. После каждой операции выводить список на экран
# Создать еще один список произвольного содержания.
# Расширить первый список вторым.
# Вставить 123 пятым элементом.
# Вывести на экран длину итогового списка.

my_listt = [0, 111, 222, 333]
print(my_listt)

my_listt_02 = [999, 888, 777, 666]
print(my_listt_02)

my_listt.extend(my_listt_02)
print(my_listt)

my_listt.insert(4, 123)
print(my_listt)

print(len(my_listt))

