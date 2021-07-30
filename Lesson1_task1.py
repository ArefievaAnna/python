#Поработайте с переменными, создайте несколько, выведите на экран,
#запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = 'Anna'
age = 44
print(f'Hello, {name}! You are {age}')

user_name = input("Enter your name")
user_id = int(input("Enter your user ID "))
user_email = input("Enter your email address")
user_password = input("Enter your password ")
print(f'Hi, {user_name}! Check your data:')
print(f'Your ID -  {user_id}, your email - {user_email}, your password - {user_password}')
