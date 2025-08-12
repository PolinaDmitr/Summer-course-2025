x = int(input())
if x % 2 == 0:
    x = x ** 0.5
else:
    x = x ** 2
print(x)

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = b * b - 4 * a * c
if d > 0:
    print('x1 =', (-b + d ** 0.5)/(2 * a))
    print('x2 =', (-b - d ** 0.5)/(2 * a))
elif d == 0:
    print('x =', (-b) / (2 * a))
else:
    print('Нет корней')

if d > 0:
    print('x1 =', (-b + d ** 0.5) / (2 * a))
    print('x2 =', (-b - d ** 0.5) / (2 * a))
else:
    if d == 0:
        print('x =', (-b) / (2 * a))
    else:
        print('Нет корней')

a = int(input())
if a > 5:
    print(a)
    print('>')
else:
    print(-a)
    print('<')
print('jnoiew')
