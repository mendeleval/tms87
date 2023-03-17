# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
#
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)
#
# предоставить 2 решения. Одно с использованием цикла while, другое с использованием цикла for с параметром.
# Оба решения предоставить в одном файле.

my_dict = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
}

for key, value in list(my_dict.items()):
    new_key = key + str(len(key))
    my_dict.update({new_key: value})
    my_dict.pop(key)

print(my_dict)

# //////////////////// - while
my_dict = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
}
key_list = list(my_dict.keys())
counter = 0

while counter != len(key_list):
    s = key_list[counter] + str(len(key_list[counter]))
    my_dict.update({s: my_dict[key_list[counter]]})
    my_dict.pop(key_list[counter])
    counter += 1

print(my_dict)


my_dict = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
}

keys = list(my_dict.keys())

for key in keys:
    new_key = key + str(len(key))
    my_dict[new_key] = my_dict.pop(key)

print(my_dict)


