""" Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""


"""with open("test_3.txt") as my_file:
    lines = 0
    letters = 0
    for line in my_file:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")"""

"""with open('test_3.txt') as my_file:
    lines = my_file.readlines()


with open('test_3.txt', 'w') as my_file:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        my_file.write('Line number {} has {} words.\n'.format(index + 1, number_of_words))


with open('test_3.txt', 'r') as f:
    amount = line.count.strip() - len(count.split())
               for line, count in enumerate(f, 1)
    lines_amount = len(amount)
print( )"""

file = open('test_3.txt')
line = 0
for i in file:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'symbols', word, 'words')

print(line, 'string')
file.close()


