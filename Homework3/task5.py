# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

with open('numbers5', 'r') as data:
    numbers = data.readlines()
print(numbers)

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


def odd_numbers(numbers):
    odd_num = []
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            odd_num.append(numbers[i])
    return odd_num


print(numbers)
x = odd_numbers(numbers)
print(x)

with open('numbers5', 'w') as data:
    for i in range(len(x)):
        data.writelines(str(x[i])+"\n")
