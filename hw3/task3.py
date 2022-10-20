# 3. Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def func(list):

    list = [1.1, 1.2, 3.1, 5, 10.01] 
    max = abs(list[0]) % 1
    min = abs(list[0]) % 1

    for i in range(1, len(list)):
        if isinstance(list[i], int):
            continue

        if max < abs(list[i]) % 1:
            max = abs(list[i]) % 1
            
        if min > abs(list[i]) % 1:
            min = abs(list[i]) % 1

    # print(f'{max}, {min}')
    d = round(max - min, 2)
    print(d)

if __name__ == '__main__':
    func(list)
