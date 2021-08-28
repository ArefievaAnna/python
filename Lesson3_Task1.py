""" Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. """


def my_func(x, y):

    try:
        x, y = int(x), int(y)
        z = x / y
    except ValueError:
        return "You can enter only numbers"
    except ZeroDivisionError:
        return "Wrong divider! You can't use zero as a divider"
    return round(z, 2)


print(my_func((input("Enter x = ")), (input("Enter y = "))))
