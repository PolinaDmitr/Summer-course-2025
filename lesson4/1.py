def f(x_, y_):
    return x_ % 10 == y_ % 10

def f1(x_, a_):
    return ((not f(x_, 5)) and f(x_, 4)) <= (x_ > a_ - 11)


for a in range(1, 500):
    if all(f1(x, a) for x in range(1, 5000)):
        print(a)