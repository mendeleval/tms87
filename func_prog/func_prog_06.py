# Дан список имен, отфильтровать все имена, где есть буква o
#
# [‘Kate’, ‘Kolya’, ‘Alex’] -> [‘Kolya’]

my_list = ["Kate", "Kolya", "Alex"]
new_list = []

for i in my_list:
    if 'o' in i:
        new_list.append(i)
print(new_list)

# ||||||||||||||||

new_name_list = list(filter(lambda x: 'o' in x, my_list))

# ||||||||||||||||
