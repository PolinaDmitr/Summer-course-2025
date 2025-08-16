def f(n):
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return l

def f2(n):
    l = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            l.append(i)
    l.append(n)
    return l

def f3(n):
    l = [1, n]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            l.append(i)
            x = n // i
            if i != x and n % x == 0:
                l.append(x)
    l.sort()
    return l



print(f(10))
print(f(100))
# print(f(726827195))
# print(f(726827190780938210)) #очень долго
print(f2(10))
print(f2(100))
# print(f2(726827195))
print(f(36))
print(f(40))
print(f3(36))
print(f3(40))
print(f3(726827195))
print(f3(726827190780938210))