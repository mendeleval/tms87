# Запросить у пользователя возраст.
# Если возраст меньше 0 - вывести Wrong input, если меньше 18 - вывести Cola, иначе - вывести Beer

text = int(input('Введите свой возраст: '))
if text < 0:
    print('Wrong input')
elif text < 18:
    print('Cola')
else:
    print('Bear')