#2. задайте натуральное число n. напишите программу, которая составит список простых множителей числа n.

n = int(input('Введите число: '))
list = []
i = 2
for j in range(n):
    while n > 2:
        while n % i == 0:
                list.append(i)
                n //= i
        i += 1
print(list)
