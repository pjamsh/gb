#3. задайте последовательность чисел. напишите программу, которая выведет список неповторяющихся элементов 
#исходной последовательности.

from random import randrange


def count_of_numbers(count):
   list_numbers = []
   for i in range(count):
       list_numbers.append(randrange(count))
   return list_numbers

def non_repeat_elements(list_numbers):
   return set(list_numbers)

all_list = count_of_numbers(int(input('Длина списка: ')))
print(all_list)
print(non_repeat_elements(all_list))
