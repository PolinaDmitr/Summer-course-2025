from string import ascii_uppercase, digits


def f(n, o):
    a = digits + ascii_uppercase
    result = ''
    while n != 0:
        result = a[n % o] + result
        n //= o
    return result


print(f(197, 18))
