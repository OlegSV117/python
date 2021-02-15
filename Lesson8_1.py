#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data1):
        # Инициализация свойств.
        self.data1 = data1

    @classmethod
    def method1(cls, data1):
        return list(map(int, data1.split("-")))


    @staticmethod
    def method2(data1):
        v=Data.method1(data1)
        print(f"Вы ввели {v}")
        if v[0]<0 or v[0]>31:
            print(f"данные по числу введены вне диапазона, введено {v[0]}")
        else:
            print(f"данные по числу введены правильно, введено {v[0]}")
        if v[1]<0 or v[0]>12:
            print(f"данные по месяцу введены вне диапазона, введено {v[1]}")
        else:
            print(f"данные по месяцу введены правильно, введено {v[1]}")
        if v[2]<1999 or v[2]>2100:
            print(f"данные по году введены вне диапазона, введено {v[2]}")
        else:
            print(f"данные по году введены правильно, введено {v[2]}")


Data.method2("12-04-2012")
Data.method2("13-00-3002")


