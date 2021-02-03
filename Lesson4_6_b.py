# Урок 4. Задание 6. Реализовать два небольших скрипта:
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
def my_cycle(b, stop):
    from itertools import cycle
    i,el =0,[]
    for c in cycle(b):
        el.append(c)
        i+=1
        if i == stop:
            yield el


 # вызов
import Lesson4_6_b as my
x=[12,3,2, "wewe"]
for el in my.my_cycle(x, 10):
    print(el)
