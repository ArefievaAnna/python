"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv


def sal():
    try:
        working_hours, rate_per_hour, bonus = map(float, argv[1:])   # sliced list argv to remove path of file
        # see documentation about built-in functions¶
        print(f'заработная плата сотрудника - {working_hours * rate_per_hour + bonus}')

    except ValueError:
        return print('Not correct format of entered data')


sal()
