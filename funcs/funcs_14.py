# Описать функцию fact2( n ), вычисляющую двойной факториал
# :n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное.
# С помощью этой функции найти двойные факториалы пяти данных целых чисел
def fact2(*args):
    for a in args:
        counter = 1
        if a % 2 == 0:
            for i in range(1, a + 1, 2):
                counter *= i

        if a % 2 != 0:
            for j in range(2, a + 1, 2):
                counter *= j
        print(counter)

fact2(6, 7, 8, 23 ,10)

