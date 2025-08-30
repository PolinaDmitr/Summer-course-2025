from string import ascii_uppercase, digits


def f(n, o):
    a = digits + ascii_uppercase
    result = ''
    while n != 0:
        result = a[n % o] + result
        n //= o
    return result

def f1(n):
    c = 0
    while n != 0:
        if n % 11 == 0:
            c += 1
        n //= 11
    return c


numb = 9 * 11 ** 210 + 8 * 11 ** 150
for x in range(3000, 0, -1):
    s = f(numb - x, 11)
    if s.count('0') == 60:
        print(x)
        break

numb = 9 * 11 ** 210 + 8 * 11 ** 150
for x in range(3000, 0, -1):
    if f1(numb - x) == 60:
        print(x)
        break