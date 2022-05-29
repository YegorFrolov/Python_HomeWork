# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части
# элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


spisok_float = [1.1, 1.2, 3.1, 5, 10.01]


def sort(list_float):
    for i in range(0, len(list_float)):
        if list_float[i] % 1 != 0:
            list_float[i] = float('0.'+(str(list_float[i]).split('.'))[1])
            if i == 0:
                max = list_float[i]
                min = list_float[i]
            if max < list_float[i]:
                max = list_float[i]
            if min > list_float[i]:
                min = list_float[i]
    return max-min


print(f'результат -{sort(spisok_float)}')
