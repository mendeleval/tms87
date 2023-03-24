# Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”

result = (lambda x, y: x + y)('Hello, ', input('name -'))
print(result)