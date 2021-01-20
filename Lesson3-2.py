# Урок 3. Задание 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def my_fun(name, last_name, year_of_birth, city, email, phone):
    print(
        f"Name: {name}; Last name: {last_name}; Year of birth: {year_of_birth}, City: {city}, Email:{email}, Phone number: {phone}")


my_fun(name="Oleg", last_name="Vasilyev", year_of_birth="1900", city="Moscow", email="12121@mail.ru",
       phone="1211212121")
