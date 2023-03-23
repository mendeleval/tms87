# Написать программу для нахождения факториала.
# Факториал натурального числа n определяется как произведение всех натуральных чисел от 1 до n включительно

def factorial(n):
    desired = 1
    for i in range(1, n + 1):
        desired *= i
    print(desired)


factorial(int(input('enter number - ')))
