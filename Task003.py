# Подсчитать сумму цифр в вещественном числе.

from random import uniform

n = round(uniform(1, 100), 3) #число от 1 до 100 с 3я знаками после запятой


def sum_digit(n):
    return sum(map(int, list(str(n).replace('.', ''))))

print(n)
print(sum_digit(n))
