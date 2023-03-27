# Дан словарь, создать новый словарь, поменяв местам ключ и значение

my_dict = {"key1": 12, "key2": 15, 'key3': 18}

new_dict = {value: key for key, value in my_dict.items()}
print(new_dict)


# new_dict_1 = {"key1": 12, "key2": 15, 'key3': 18}
# for key, value in new_dict_1.items():
#     new_dict_1[value] == key
# print(new_dict_1)
#

