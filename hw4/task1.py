#1. вычислить число c заданной точностью d
#пример:
#при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

def func(num):
   count = 0
   while int(num) < 1:
       num *= 10
       count += 1
   return count


if __name__ == '__main__':
   d = float(input('Введите дробную часть числа с необходимой точностью (формат: 0.0001): '))
   number = float(input('Введите ваше чило: '))
   number = round(number, func(d))
   print(f'Ваше число с заданной точностью: {number}')
