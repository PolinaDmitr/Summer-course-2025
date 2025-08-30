from math import gcd

def f(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        print('a, b=', a, b)
    return a + b

print(f(76, 8))
print(gcd(76, 8))