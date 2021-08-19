"""Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

lines = []
while True:
    line = input("Enter any text: ")
    if line == '':
        print(lines)
        exit()
    else:
        newline = line
        lines.append(newline)

    with open("test.txt", "w") as my_file:
        my_file.writelines("%str\n" % line for line in lines)
