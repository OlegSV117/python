# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Сomplex_number:
    def __init__(self, c):
        self.c = c

    def __add__(self, other):
        return self.c.real + other.c.real + (self.c.imag + other.c.imag) * 1j

    def __mul__(self, other):
        return self.c.real * other.c.real - self.c.imag * other.c.imag + (
                    self.c.real * other.c.imag + other.c.real * self.c.imag) * 1j


a = Сomplex_number(complex(7, 8))
b = Сomplex_number(complex(1, 2))

print(a + b)
''' проверка сложения'''
print(complex(7, 8) + complex(1, 2))

print(a * b)
''' проверка умножения'''
print(complex(7, 8) * complex(1, 2))
