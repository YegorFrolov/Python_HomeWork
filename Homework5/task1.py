#  Напишите программу, удаляющую из текста все слова содержащие "абв",
#  которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции.
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

text_in= 'бвгдеж рабав копыто фабв Абкн абрыволк аБволк'
deleted_text = 'абв'
lower_text = text_in.lower()

def cleaned_text (filter_text):
    text_clean = list(filter(lambda x : deleted_text not in x,filter_text.split()))
    return ' '.join(text_clean)

print(cleaned_text(lower_text))





