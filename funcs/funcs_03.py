# Написать программу для нахождения факториала.
# Факториал натурального числа n определяется как произведение всех натуральных чисел от 1 до n включительно

def factorial(n):
    desired = 1
    for i in range(1, n + 1):
        desired *= i
    return desired


def main():
    print(factorial(int(input('enter num - '))))


if __name__ == "__main__":
    main()
