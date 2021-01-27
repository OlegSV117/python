# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

try:
    with open("text_4.txt", 'r', encoding="utf-8") as f_E:
        f_R = open("text_4_1.txt", 'a', encoding="utf-8")
        my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        for el in f_E.readlines():
            print((my_dict.get(el.split(' - ')[0]) ) + ' - ' + (el.split(' - ')[1].replace('\n','')), file=f_R)
    f_R.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
