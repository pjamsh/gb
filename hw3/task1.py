# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

new_list = [2, 6, 34, 8, 4]
sum = 0

for i in range(0, len(new_list)):
    if i % 2 != 0:
        sum += new_list[i]

print(new_list)
print(sum)
