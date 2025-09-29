# Палиндром
# Пользователь вводит строку.
# Переводим её либо в нижний, либо в верхний регистр
# и проверяем является ли строка палиндромом.


string = input('Введите любую строку: ')

print(string.lower())
reversed_string = string.lower()[::-1]
print(reversed_string)

if string.lower() == reversed_string:
    print('Строка является палиндромом')
else:
    print('Строка не является палиндромом')