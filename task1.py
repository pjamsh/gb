#1. вычислить число c заданной точностью d
#пример:
#при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

#2. задайте натуральное число n. напишите программу, которая составит список простых множителей числа n.

#3. задайте последовательность чисел. напишите программу, которая выведет список неповторяющихся элементов 
#исходной последовательности.

#4. задана натуральная степень k. сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
#и записать в файл многочлен степени k.
#пример:
#k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

#5. даны два файла, в каждом из которых находится запись многочлена. задача - сформировать файл, содержащий сумму многочленов.


#1
#def func(num):
#    count = 0
#    while int(num) < 1:
#        num *= 10
#        count += 1
#    return count


#if __name__ == '__main__':
#    d = float(input('введите дробную часть числа с необходимой точностью (формат: 0.0001): '))
#    number = float(input('введите ваше чило: '))
#    number = round(number, func(d))
#    print(f'ваше число с заданной точностью: {number}')


#3
#from random import randrange


#def count_of_numbers(count):
#    list_numbers = []
#    for i in range(count):
#        list_numbers.append(randrange(count))
#    return list_numbers

#def non_repeat_elements(list_numbers):
#    return set(list_numbers)

#all_list = count_of_numbers(int(input('list len: ')))
#print(all_list)
#print(non_repeat_elements(all_list))


#4
#from random import randint

#def func(k):
#    file = open('C:\Users\User\source\repos\python\task1\task1\file.txt', 'w')
#    a = int(0)

#    for i in range(-k, -1):

#        a = randint(1, 101)
#        if a!= 0:
#            file.write(str(a))
#            file.write('* x ^ ')
#            file.write(str(-i))
#            file.write('+')

#    a = randint(1, 101)
#    if a != 0:
#        file.write(str(a))
#            file.write('* x + ')
    
#    a = randint(1, 101)
#    if a != 0:
#        file.write(str(a))

#    file.write('= 0')

#    file.close



#chislo = int(input('Print k: '))
#func(chislo)


#5
#def read_file():
#    eq1 = open_file(text.txt)
#    print('Первый многочлен: ', eq1)
#    eq1 = eq1[:-2].split('+')
#    eq2 = open_file('text1.txt')
#    print('Второй многочлен: ', eq2)
#    eq2 = eq2[:-2].split('+')

#    dict1 = separate_equa(eq1)
#    dict2 = separate_equa(eq2)

#    #
#    if len(dict1.keys()) > len(dict2.keys()): 
#        normalize(addition_eq(dict1, dict2))
#    else:
#        normalize(addition_eq(dict2, dict1))


#def open_file(name):
#    f = open(name, 'r')
#    equa = f.read()
#    f.close
#    return equa


#def separate_equa(equa):
#    dict_eq = {}
#    for el in equa:
#        if el.rfind('^') != -1:
#            key = int(el[int(el.rfind('^')) + 1:])
#            value = int(el[:int(el.find('*'))])

#        elif el.rfind('x') != -1:
#            key = 1
#            value = int(el[:int(el.find('*'))])

#        else:
#            key = 0
#            value = int(el)

#        dict_eq[key] = value
#    return dict_eq


#def addition_eq(dict1, dict2):
#    res_dict = {}

#    for key in dict1:
#        if (key in dict1) and (key in dict2):
#            res_dict[key] = dict1[key] + dict2[key]
#        elif (key in dict1) and (key not in dict2):
#            res_dict[key] = dict1[key]
#        elif (key in dict2) and (key not in dict1):
#            res_dict[key] = dict2[key]
#    return res_dict


#def normalize(res_dict):
#    equa = ''
#    for key in res_dict:
#        if key == 0:
#            equa = equa + '+' + str(res_dict[key]) + '= 0'
#        elif key == 1:
#            equa = equa + '+' + str(res_dict[key]) + 'x'
#        else:
#            equa = equa + '+' + str(res_dict[key]) + '* x ^' + str(key)

#    print('Сумма многочленов: ', equa)
#    f = open('result.txt', 'w')
#    f.write(equa)
#    f.close()

#if __name__ == '__main__':
#    read_file()          


n = int(input())
i = 2
while n > 2:
    while n % i == 0:
        print(i, end = ' ')
        n //= i
    i += 1

