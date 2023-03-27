# Пользователь вводит три числа. Увеличьте первое число в два раза, второе
# числа уменьшите на 3, третье число возведите в квадрат и затем найдите
# сумму новых трех чисел.

print('Введите три числа')
first_number = int(input())
second_number = int(input())
third_number = int(input())

first_number_processed = (first_number * 2)
second_number_processed = (second_number - 3)
third_number_processed = (third_number ** 2)

print(f'{first_number_processed}\n{second_number_processed}\n{third_number_processed}')

sum_of_numbers = first_number_processed + second_number_processed + third_number_processed
print(f'Сумма введенных чисел: {sum_of_numbers}')