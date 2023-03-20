# Получить на ввод количество рублей и копеек и вывести в правильной форме,
# например, 3 рубля, 1 рубль 25 копеек, 3 копейки

my_rub = int(input('Введите кол-во рублей: '))
my_cen = int(input('Введите кол-во копеек: '))

if (my_rub != 0) and (my_cen != 0):
    print(f'{my_rub} rub. {my_cen} cen')
elif (my_rub != 0) and (my_cen == 0):
    print(f' {my_rub} rub.')
else:
    print(f'{my_cen} cen.')
