# Пользователь вводит значение температуры в градусах Цельсия. Вывести температуру  в градусах Фаренгейта.

print('Введите температуру в градусах Цельсия: ')
degrees_сelsius = int(input())
degrees_fahrenheit = (degrees_сelsius * 1.8) + 32
print(f'Температура в градусах Фаренгейта: {degrees_fahrenheit}')