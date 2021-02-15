# Урок2. Задание 2.
# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
# my_list = list([input("Введите элемент списка:")])

my_list = input("Введите элементы списка через пробел:").split()
result_list = []
for i in range(0, len(my_list) - 1, 2):
    result_list.append(my_list[i + 1])
    result_list.append(my_list[i])
if len(my_list) % 2 != 0:
    result_list.append(my_list[len(my_list) - 1])
print("Исходный список", my_list)
print("Модифицированный список", result_list)
