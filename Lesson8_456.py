# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад
# и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники»
# максимум возможностей,изученных на уроках по ООП.

class Storage():
    def __init__(self, equipment, name, number):
        self.equipment= equipment
        self.name = name
        self.number = number

    def my_Storage(self):
        if self.equipment == "printer":
            Printer.my_Printer()
        if self.equipment == "scanner":
            Scanner.my_Scanner()
        if self.equipment == "copier":
            Copier.my_Copier()

class Office_Equipment:
    def __init__(self,equipment, name, number):
        self.equipment = equipment
        self.name = name
        self.number = int(number)

class Printer(Office_Equipment):
    def __init__(self,name, number, dict_Printer):
        super().__init__(name,number)
        self.dict_Printer = dict_Printer

    def my_Printer(self, name, number):
        return self.dict_Printer.update({name, number})


class Scanner(Office_Equipment):
    def __init__(self, name, number,dict_Scanner):
        super().__init__(name, number)
        self.dict_Scanner = dict_Scanner

    def my_Scanner(self, name, number):
        return self.dict_Scanner.update({name, number})

class Copier(Office_Equipment):
    def __init__(self, name, number,dict_Copier):
        super().__init__(name, number)
        self.dict_Copier = dict_Copier

    def my_Copier(self,name, number):
        return self.dict_Copier.update({name, number})

a=Storage("printer", "Sumsung", 3)
print(a.dict_Printer())


