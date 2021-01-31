# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки", self.title)


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки", self.title)


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки", self.title)


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки", self.title)


а_Stationery = Stationery("канцелярской принадлежностью")
а_Stationery.draw()
print(а_Stationery.title)

а_Pen = Pen("ручкой")
а_Pen.draw()
print(а_Pen.title)

а_Pencil = Pencil("капандашом")
а_Pencil.draw()
print(а_Pencil.title)

а_Handle = Handle("маркером")
а_Handle.draw()
print(а_Handle.title)
