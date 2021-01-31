# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
try:
    with open("Lesson5_5.txt", 'x') as f_obj:
        my_number = input("Ведите числа через пробел:")
        f_obj.write(my_number + ' ')
        s = 0.0
        for item in my_number.split():
            s += float(item)
        print('сума чисел', s)
except IOError:
    print("Произошла ошибка ввода-вывода!")
except ValueError:
    print("Вы ввели не числа!")
