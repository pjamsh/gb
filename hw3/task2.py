# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

def multiplication(our_list):
    if len(our_list) % 2 == 0:
        for i in range(0, (len(our_list) // 2)):
            mult = our_list[i] * our_list[-i - 1]
            created_list.append(mult)

    else:
        for i in range(0, (math.ceil(len(our_list) / 2))):
            mult = our_list[i] * our_list[-i - 1]
            created_list.append(mult)

    return created_list

if __name__ == '__main__':
    our_list = [3, 5, 7, 21, 6, 7, 2]
    created_list = []
    mult = 1
    print(multiplication(our_list))
