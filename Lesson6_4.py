# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.is_police == True:
            police = "Полицейская"
        else:
            police = ""

        if self.speed > 0:
            print(f"{police} Машина {self.color} {self.name} поехала")

    def stop(self):
        if self.is_police == True:
            police = "Полицейская"
        else:
            police = ""
        if self.speed == 0:
            print(f"{police} Машина {self.color} {self.name} остановилась")

    def turn_direction(self, direction):
        if self.is_police == True:
            police = "Полицейская"
        else:
            police = ""
        if self.speed > 0:
            print(f"{police} Машина {self.color} {self.name} повернула {direction}")

    def show_speed(self):
        if self.is_police == True:
            police = "Полицейская"
        else:
            police = ""
        print(f"{police} Машина {self.color} {self.name} едет на скорости {self.speed} км/час")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.color} {self.name} превышает скорость 60 км/час")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.color} {self.name} превышает скорость 40 км/час")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

a_Car = Car(100, 'Зеленый', 'Фольцваген', False)
a_Car.go()
a_Car.stop()
a_Car.turn_direction("Направо")
a_Car.show_speed()
print(a_Car.speed)
print(a_Car.color)
print(a_Car.name)
print(a_Car.is_police)
#
a_TownCar = TownCar(100, 'Синяя', 'Лада', False)
a_TownCar.go()
a_TownCar.stop()
a_TownCar.turn_direction("Направо")
a_TownCar.show_speed()
print(a_TownCar.speed)
print(a_TownCar.color)
print(a_TownCar.name)
print(a_TownCar.is_police)
#
a_SportCar = SportCar(300, 'Красная', 'Феррари', False)
a_SportCar.go()
a_SportCar.stop()
a_SportCar.turn_direction("Направо")
a_SportCar.show_speed()
print(a_SportCar.speed)
print(a_SportCar.color)
print(a_SportCar.name)
print(a_SportCar.is_police)
#
a_WorkCar = WorkCar(0, 'Желтый', 'Подметальщик', False)
a_WorkCar.go()
a_WorkCar.stop()
a_WorkCar.turn_direction("Налево")
a_WorkCar.show_speed()
print(a_WorkCar.speed)
print(a_WorkCar.color)
print(a_WorkCar.name)
print(a_WorkCar.is_police)
#
a_PoliceCar = PoliceCar(150, 'Белый', 'Мерседес', True)
a_PoliceCar.go()
a_PoliceCar.stop()
a_PoliceCar.turn_direction("Налево")
a_PoliceCar.show_speed()
print(a_PoliceCar.speed)
print(a_PoliceCar.color)
print(a_PoliceCar.name)
print(a_PoliceCar.is_police)
