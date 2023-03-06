# Ввести число, проверить на то, что было введено именно число.
# Возвести его в куб и вывести результат на экран.

text = input('Введите число: ')
text_digit = text.isdigit()

if text_digit == True:
    print(int(text) ** 3)

elif text_digit == False:
    print('NO INT')