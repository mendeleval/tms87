# Ввести строку. Если длина строки больше 10 символов,
# то создать новую строку с 3 восклицательными знаками в конце  ('!!!') и вывести на экран.
# Если меньше 10, то вывести на экран второй символ строки

my_str = input("Введите строку - ")
my_str_len = len(my_str)
if my_str_len > 10:
    print(f'{my_str} !!!')
elif my_str_len < 10:
    print(my_str[1])