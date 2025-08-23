def f(x_, y_, a_):
    return (x_ * y_ > a_) or (x > y) or (11 > x)

for a in range(120, 125):
    flag = True
    for x in range(1, 10000):
        for y in range(1, 10000):
            if not f(x, y, a):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)