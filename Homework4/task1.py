# Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.
import random


def filth_random ():
    with open("text_for_task1 ", "w") as file:
        for i in range(0 , 10):
            file.write(str(random.randint(-1000, 1000))+'\n')

filth_random()

def sorting_file():
    with open("text_for_task1 ", "r") as file:
        elements_list = [int(x) for x in file.readlines()]
        elements_list=sorted(elements_list)
    with open("text_for_task1 ", "w") as file:
        for num in elements_list:
            file.write(str(num) + '\n')

sorting_file()