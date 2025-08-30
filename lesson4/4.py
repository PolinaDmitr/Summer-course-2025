from math import gcd

def f(a_, x_):
    return (gcd(a_, 420) == 2) or ((gcd(a_, x_) != 12) <= (gcd(110, x_) != 11))


c = 0
for a in range(1000):
    if all(f(a, x) for x in range(1, 2000)):
        print(a)
        c += 1
print('c=', c)