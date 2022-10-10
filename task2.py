# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('N = '))
comp = 1
list = []

for i in range (1, N + 1):
    comp *= i
    list.append(comp)
print(list)