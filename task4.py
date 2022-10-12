# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# свой вариант

from random import randint
import random

N = int(input('N = '))
list = []
list2 = []
proisv = 1

data = open('file.txt', 'w')

for j in range(N):
    rnd = random.randint(1, N+1)
    data.writelines(str(rnd) + '\n') 

for i in range(N):
    list.append(randint(-N, N))
    list2.append(list[i] * rnd)
print(list)
print(list2)

data.close()
print('\n')

# посмотрел семинар и понял, как должно быть
from random import randint

def func(N):
    list = []
    mult = 1

    for i in range(N):
        list.append(randint(-N, N))
    print(list)

    file = open('num.txt', 'r')

    for line in file:
        # print(line)
        mult *= list[int(line)]

    file.close()

    print(mult)



if __name__ == '__main__':
    func(10)

