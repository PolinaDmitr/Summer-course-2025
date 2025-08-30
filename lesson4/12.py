from string import ascii_uppercase, digits


def f(n, o):
    a = digits + ascii_uppercase
    result = ''
    while n != 0:
        result = a[n % o] + result
        n //= o
    return result


#4163×5+1262−x
numb = 4 ** 163 * 5 + 12 ** 62
for x in range(2005, 0, -1):
    n_str = f(numb - x, 5)
    if n_str.count('1') < n_str.count('4'):
        print(x)
        break