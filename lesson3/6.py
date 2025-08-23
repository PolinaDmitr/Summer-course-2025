def f(x_, y_, a_):
    return (x_ < a_) and (y_ < 3 * a_) or (2 * x_ + y_ > 128)

for a in range(64, 100):
    flag = True
    for x in range(1, 100000):
        for y in range(1, 100000):
            if not f(x, y, a):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)