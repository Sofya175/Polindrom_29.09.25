# Палиндром
# Пользователь вводит строку.
# Переводим её либо в нижний, либо в верхний регистр
# и проверяем является ли строка палиндромом.


string = input('Введите любую строку для проверки на палиндром: ').strip().lower()

#print(string.lower())
#reversed_string = string.lower()[::-1]
#print(reversed_string)

if string == string[::-1]:
    print('Строка "' + string + '" является палиндромом')
else:
    print('Строка "' + string + '" не является палиндромом')