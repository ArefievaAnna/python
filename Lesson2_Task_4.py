# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_str = input("enter few words with space ")
user_word = []
num = 1
for el in range(user_str.count(' ') + 1):
    user_word = user_str.split()
    if len(str(user_word)) <= 10:
        print(f" {num} {user_word [ el ]}")
        num += 1
    else:
        print(f" {num} {user_word [ el ] [ 0 :10 ]}")
        num += 1
