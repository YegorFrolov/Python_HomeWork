#
# Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с
# названиями языков программирования, другой — с числами от 1 до длины первого плюс 1.
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из
# номера и языка, написанного большими буквами. Вторая — которая отфильтрует этот список
# следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре
# в кортеже, то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется.
# Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой
# таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.


lang = ['C++', 'C#', 'Python', 'HTML', '.net', 'SQl', 'GO']
number = [i + 1 for i in range(0, len(lang))]


def zipping(num):
    upper_lang = [i.upper() for i in lang]
    zip_lang = list(zip(number, upper_lang))
    return zip_lang


print(zipping(number))

"""
вычисляем сумму очков внутри ячейки
"""

def funck_ord(rate_lang, num):
    temp_spis = []
    for i in rate_lang:
        temp_ord_num = 0
        for x in i:
            temp_ord_num += ord(x)
        temp_spis.append(temp_ord_num)
        print(temp_ord_num)

    for i in range(len(num)-1, -1, -1):
       if temp_spis[i] % num[i] == 0:
           num[i] = temp_spis[i]
       else:
           temp_spis.pop(i)
           num.pop(i)
           rate_lang.pop(i)
    return (list(zip(num, rate_lang)))

# print(rate_lang)


print(funck_ord(lang, number))


# numbers =list(enumerate(lang, start=1))
#
# print(numbers)
