# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.


text_to_finde = 'п'
text_all = 'привпривет ПРИВЕТ прив привет при привете'


def finder():
    count = 0  # вхождения
    i = 0  # i = счетчик перебора символов
    while i < (len(text_all)-len(text_to_finde)+1):
        if text_to_finde == text_all[i:i+len(text_to_finde)]:
            count += 1
            i = i+len(text_to_finde)
        else:
            i += 1
    print('кол-во вхождений- ' + str(count))


finder()
