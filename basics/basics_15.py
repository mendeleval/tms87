# Пользователь вводит время в минутах и расстояние в километрах. Найдите скорость в м/c.

print('Введите время и растояние м/к:')
time = int(input())
distance = int(input())
time_seconds = time * 60
distance_meters = distance * 1000
speed = distance_meters / time_seconds
print(f'Cкорость в м/с: {speed}')
