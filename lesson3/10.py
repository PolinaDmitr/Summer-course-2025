def f(x_, a1_, a2_):
    return (not (a1_ <= x_ <= a2_)) <= ((36 <= x_ <= 75) == (60 <= x_ <= 110))

for a1 in range(35, 112):
    for a2 in range(a1 + 1, 113):
        if all(f(x, a1, a2) for x in range(30, 120)):
            print(a1, a2, a2 - a1)