# Урок 3. Задание 1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.
def my_dev(a1, a2):
    try:
        res = a1 / a2
    except ZeroDivisionError:
        return ("Вы ввели делитель, равный нулю")
    return (round(res, 4))


while True:
    try:
        arg1 = float(input("Введите делимое:"))
        arg2 = float(input("Введите делитель:"))
        break
    except ValueError:
        print("Вы ввели не число, попробуйте еще.")
print(arg1, arg2)
print(f"Результат выполнения функции: {my_dev(arg1, arg2)}")
