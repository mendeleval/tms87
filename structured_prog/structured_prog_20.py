# В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы.

my_str = list(input('enter str - ').split(' '))
print(*my_str)
print(*my_str[::-1])