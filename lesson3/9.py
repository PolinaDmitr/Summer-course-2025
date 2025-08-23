def f(x_, a_):
    return (x_ & 57 == 0) or ((x_ & 23 == 0) <= (x_ & a_ != 0))

for a in range(1, 50):
    # l = []
    # for x in range(1, 100):
    #     l.append(f(x, a))
    l = [f(x, a) for x in range(1, 10000)]
    if all(l):
        print(a)

