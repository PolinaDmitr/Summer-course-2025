def f(x_, a1_, a2_):
    return (17 <= x_ <= 58) <= (((29 <= x_ <= 80) and not (a1_ <= x_ <= a2_)) <= (not (17 <= x_ <= 58)))


l = []
for a1 in range(16, 82):
    for a2 in range(a1 + 1, 83):
        if all(f(x, a1, a2) for x in range(100)):
            print(a1, a2, a2 - a1)
            l.append(a2 - a1)
print('A = ', min(l))