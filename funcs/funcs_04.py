# Реализовать функцию возвращающую матрицу. На вход принимает n - размерность матрицы,
# random_from(по-умолчанию 1), random_to(по-умолчанию(9))

from random import randint


def matrix(n, random_from=1, random_to=9):
    return [[randint(random_from, random_to) for _ in range(n)] for _ in range(n)]


def main():
    print(matrix(int(input('enter num - '))))


if __name__ == "__main__":
    main()
