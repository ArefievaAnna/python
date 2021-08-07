# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе.

my_list = []
my_list.extend([True, 0, 1, 2, 'string', '', 47.1, b'bytes string', {'name': 'Anna'}, bytearray(b'bates array'), (1,),
                {1, 2, 1, 3}, ValueError, None, {}])

my_list.append(my_list)

for item in my_list:
    item_type = type(item)
    print(f'{item} has {item_type} type')
