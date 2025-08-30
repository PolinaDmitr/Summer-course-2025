def f(x_, y_, a_):
    return ((a_ < x_) or (x_**2 - 7 * x_ + 10 > 0)) and ((a_ >= y_) or (y_**2 + 7 * y_ + 12 > 0))


c = 0
for a in range(500):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not f(x, y, a):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
        c += 1
print('c=', c)