# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

str_num = input('Введите вещественное число: ')
num = str_num.replace('.', '0')
num = int(num)
sum = 0

if type(num) == int:
    while num > 0:
        sum += num % 10
        num //= 10 
    print(f'Сумма цифр в числе - {sum}')

## работает только в случае десятых долей
# num = float(input('num: '))
# integer = int(num)
# sum = 0

# if num != 0:
#     num *= 10
#     middle = num - int(num)
#     if middle != 0:
#         num *= 10
#     else:
#         while num > 0:
#             sum += num % 10
#             num //= 10 
# print(int(sum))
