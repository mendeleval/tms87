# Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”
# Примечание: после ввода переменных преобразовать переменные к типу int
#  >> first_number = int(first_number)

print('Введите два числа: ')

first_number = int(input())
second_number = int(input())
result = first_number + second_number
print(f'{first_number} плюс {second_number} равно {result}')