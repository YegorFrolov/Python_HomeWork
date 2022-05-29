# Найти НОК двух чисел

num_a = int(input("введите первое число: "))
num_b = int(input("введите второе число: "))


def calc(x, y):
    if x > y:
        bigger = x
    else:
        bigger = y

    while(True):
        if ((bigger % x == 0) and (bigger % y == 0)):
            nok = bigger
            break
        bigger += 1
    return nok


print("НОК от", num_a, " и ", num_b, " = ", calc(num_a, num_b))
