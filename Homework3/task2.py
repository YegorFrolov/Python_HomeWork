# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.

# import math

# num_letter = int(input("введите точность вычисления π - "))

# Pi = math.pi

# print(round(Pi, num_letter))


import math

num_letter = input("введите точность вычисления π - ")
Pi = math.pi

'''
def - метод для подсчета знаков после точки
'''


def with_dot(number):
    count_of_symbols = abs(number.find('.') - len(number)) - 1
    return count_of_symbols


'''
выбор введено значение с точкой или просто цифра
'''

if num_letter.find(".") != -1:
    print(round(Pi, with_dot(num_letter)))
else:
    print(round(Pi, int(num_letter)))
