#Урок 4. Задание1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, name, output_in_hours, rate_per_hour, prize = argv

output_in_hours, rate_per_hour, prize = float(output_in_hours), float(rate_per_hour), int(prize)
print("Сотрудник: ", name,". Заработная плата.составляет:",(output_in_hours*rate_per_hour)+prize,"рублей.")

#скрипт для обращения к программе: python Lesson4-1.py Иванов 244 34 15000