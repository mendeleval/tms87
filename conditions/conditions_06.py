# Ввести почтовый адрес. Проверить доменное имя.
# В случае если оно gmail.com, вывести на экран имя почтового ящика.
# Иначе вывести надпись “DOMAIN NAME is not supported’

text = input('Введите почтовый адрес: ')
if "gmail.com" in text:
    print(text)

else:
    print('DOMAIN NAME is not supported')