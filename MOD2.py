# 2.2 Команды print() и input(), переменные 
# variable_name = input()
# print('Вы ввели текст:', variable_name)
# 2.3 sep, end, PEP 8
# print('aa', 'bb', 'cc', sep='*')
# minus = '-'
# print('a', 'b', 'c', end=minus)
# print('second line')
# print('a', 'b', 'c', sep='', end='')
# print('d', 'e', 'f', sep='')
# print('Python', end='\n\n\n')  # Примечание, два пробела после, знак и пробел
# 2.4 Целочисленная арифметика
# s = '1992'
# year = int(s)
# print(year)
# num = int(input())
# a = int(input())
# b = int(input())
# print(3*(a+b)*(a+b)*(a+b)+275*b*b-127*a-41)
# при 0 < n < m результатом деления n % m является число n, а результатом деления n // m является число 0.
# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)
# n = int(input())
# print(-(-n//4))
# Первая цифра: (num % 10n) // 10n-1
# Последняя цифра: (num % 10)
n = int(input())
print('Сумма цифр =', (n%10+((n//10)%10))+n//100)
print('Произведение цифр =', (n%10*((n//10)%10))*(n//100))
