# Логические операторы

# Ладья
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if b == d or a == c:
#     print('YES')
# else:
#     print('NO')

# Король
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (-1 <= (a - c) <= 1) and (-1 <= (b - d) <= 1):
#     print('YES')
# else:
#     print('NO')

# Условный оператор 

# a, b, c = int(input()), int(input()),  int(input())
# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#    print(0)

# n, k = int(input()), int(input())
# if n > k:
#    print('NO')
# elif k > n:
#    print('YES')
# else:
#    print("Don't know")

# Серединное число
# a, b, c = int(input()), int(input()),  int(input())
# if (a >= b >= c) or (c >= b >= a):
#     print(b)
# elif (b >= c >= a) or (a >= c >= b):
#     print(c)
# else:
#     print(a)
# Количество дней
# n = int(input())
# if n in [1, 3, 5, 7, 8, 10, 12]:
#     print(31)
# elif n in [4, 6, 9, 11]:
#     print(30)
# elif n == 2:
#     print(28)

# Калькулятор
# a, b = int(input()), int(input())
# c = str(input())
# if c == '+':
#     print(a+b)
# elif c == '-':
#     print(a-b)
# elif c == '*':
#     print(a*b)
# elif c == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(a/b)  
# else:
#    print('Неверная операция')


#c1, c2 = input(), input()
#if c1 in ('красный', 'синий','желтый') and c2 in ('красный', 'синий','желтый'):
#    if c1 == c2:
#        print(c1)
#    elif (c1 in ['красный', 'синий'] and c2 in ['красный', 'синий']):
#        print('фиолетовый')
#    elif (c1 in ['красный', 'желтый'] and c2 in ['красный', 'желтый']):
#        print('оранжевый')
#    elif (c1 in ['синий', 'желтый'] and c2 in ['синий', 'желтый']):
#       print('зеленый')
#else: 
#    print('ошибка цвета')

# Цвета колеса рулетки

#n = int(input())
#r = 'красный'
#b = 'черный'
#if 0 <= n <= 36:
#    if n == 0:
#        print('зеленый')
#    elif n in range(1, 11) or n in range(19, 29):
#        if n%2 == 0:
#            print(b)
#        else:
#            print(r)   
#    elif n in range(11, 19) or n in range(29, 37):
#        if n%2 == 0:
#            print(r)
#        else:
#            print(b)        
#else:
#    print('ошибка ввода')

# Пересечение отрезков

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 == a2:
    print(b1)
elif b2 == a1 and b1 != a2:
    print(b2)
elif b1 == a2 and b2 != a1:
    print(b1)
elif a1 <= a2 <= b2 <= b1:
    print(a2, b2)
elif a2 <= a1 <= b1 <= b2:
    print(a1, b1)
elif a1 <= a2 <= b1:
    print(a2, b1)
elif a2 <= a1 <= b2:
    print(a1, b2)
elif (a1 not in range(a2, b2+1) and b1 not in range(a2, b2+1)) or (a2 not in range(a1, b1+1) and b2 not in range(a1, b1+1)):
    print('пустое множество')