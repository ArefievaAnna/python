my_list = [3, 18, 2, 2, 3, 5, 67]
my_new_list = [el for el in my_list if not my_list.count(el) != 1]
print(f'итоговый массив чисел  {my_new_list}')
