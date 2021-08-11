""" Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):

    arguments = [arg1, arg2, arg3]
    try:
        arguments.remove(min(arguments))
        return sum(arguments)
    except TypeError:
        return "You should enter only numbers! "


print(my_func(3, 8, 7))


# second solution

def my_func(arg1, arg2, arg3):

    try:
        my_list = [int(s) for s in input().split()]
        my_list.remove(min(my_list))
        return sum(my_list)
    except ValueError:
        return "You should enter only numbers! "


print(my_func(input("Enter arg1"), input("Enter arg2"), input("Enter arg3")))

