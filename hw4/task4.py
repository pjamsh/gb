#4. задана натуральная степень k. сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
#и записать в файл многочлен степени k.
#пример:
#k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint


def func(k):
   file = open('file.txt', 'w')
   a = int(0)

   for i in range(-k, -1):

       a = randint(1, 101)
       if a!= 0:
           file.write(str(a))
           file.write('*x^')
           file.write(str(-i))
           file.write(' + ')

   a = randint(1, 101)
   if a != 0:
       file.write(str(a))
       file.write('*x + ')
    
   a = randint(1, 101)
   if a != 0:
       file.write(str(a))

   file.write(' = 0')

   file.close


chislo = int(input('Print k: '))
func(chislo)
