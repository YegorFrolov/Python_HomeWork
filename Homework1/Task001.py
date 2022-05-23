# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


number = int(input('введите число членов - '))
list_Spis = []


def spisok(number_N):
    for i in range(0, number_N, 1):  # от 0 до number_N с шагом 1
        list_Spis.append((-3)**i)
    print(list_Spis)


spisok(number)


# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
