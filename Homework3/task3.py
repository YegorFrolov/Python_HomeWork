# Составить список простых множителей натурального числа N
import math


def prime(n):
    # делим четное число => нечетное
    while n % 2 == 0:
        print(2),
        n = n / 2

    # n становится не четным
    for i in range(3, int(math.sqrt(n))+1, 2):

        while (n % i == 0):
            print(i)
            n = n / i

    if n > 2:
        print(n)


num = int(input("Введите число для нахождения простых множителей : "))
prime(num)
