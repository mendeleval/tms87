# Написать функцию, которая получает на вход имя и выводит строку вида: “Hello, {name}”.
# Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.


# def my_func():
#     arr = ["Dima", "Maksim", "Valera", "Ira", "Valik"]
#     for i in arr:
#         print(f'Hello {i}')
#
# my_func()

# Сделать через main

def my_func(name: str):
    print(f'Hello {name}')


def main():
    arr = ["Dima", "Maksim", "Valera", "Ira", "Valik"]
    for i in arr:
        my_func(i)


if __name__ == '__main__':
    main()
