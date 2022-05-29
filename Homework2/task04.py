# Написать программу преобразования десятичного числа в двоичное

number_des = int(input("Введите число: "))
number_2d = ''

while number_des > 0:
    number_2d = str(number_des % 2) + number_2d
    number_des = number_des // 2

print(number_2d)
