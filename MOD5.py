# n = int(input())
# if n%100 == 0:
#    print('YES')
# else:
#    print('NO')

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if ((a%2 == 0 and b%2 == 0) or (a%2 != 0 and b%2 != 0)) and ((c%2 == 0 and d%2 == 0) or (c%2 != 0 and d%2 != 0)):
#     print('YES')
# elif ((a%2 == 0 and b%2 != 0) or (a%2 != 0 and b%2 == 0)) and ((c%2 == 0 and d%2 != 0) or (c%2 != 0 and d%2 == 0)):
#     print('YES')
# else: 
#     print('NO')

# age = int(input())
# sex = input()
# if 10 <= age <= 15 and sex == 'f':
#     print('YES')
# else: 
#     print('NO')

#n = int(input())
#if 1 <= n <= 10:
#    if n in [1, 2, 3]:
#        print('I'*n)
#    elif n == 4:
#        print('IV')
#    elif n in [5, 6, 7, 8]:
#        print('V'+'I'*(n-5))
#    elif n == 9:
#        print('IX')
#    else:
#        print('X')
#else:
#    print('ошибка')

# n = int(input())
# if n%2 == 0 and ( 2 <= n <= 5 or n > 20):
#     print('NO')
# elif (n%2 == 0 and 6 <= n <= 20) or (n%2 != 0):
#     print('YES')

# Ход слона
# a, b, c, d = int(input()), int(input()), int(input()), int(input())  
# if a == c or b == d:
#     print('NO')
# elif ((a-c == b-d) or (a-c == d-b)) or ((c-a == d-b) or (c-a == b-d)):
#     print('YES')
# else:
#     print('NO')

# Ход коня...
# a, b, c, d = int(input()), int(input()), int(input()), int(input())  
# if a == c and b == d:
#     print('NO')
# elif ((a-c)**2 == 1 and (b-d)**2 == 4) or ((a-c)**2 == 4 and (b-d)**2 == 1):
#     print('YES')
# else:
#    print('NO')

# Ход ферзя...............
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a-c)**2 == (b-d)**2 or (a == c and b != d) or (a != c and b == d):
    print('YES')
else: print('NO')