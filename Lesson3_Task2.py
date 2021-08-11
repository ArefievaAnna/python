""" Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой """


name = input('Please, enter your name')
surname = input('Please, enter your surname')
year = input('Please, enter your birth year')
city = input('Please, enter your city')
email = input('Please, enter your email')
phone_number = input('Please, enter your phone number')


def my_func(name, surname, year, city, email, phone_number):
    return ' '.join([name, surname, year, city, email, phone_number])


print(my_func(surname, name, year, city, email, phone_number))
