# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

from itertools import accumulate
import operator

N = int(input('Введите число: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))


print(get_prods(N))
