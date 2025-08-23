#& - поразрядная конъюнкция
print(bin(14)[2:].zfill(4))
print(bin(5)[2:].zfill(4))
print(bin(4)[2:].zfill(4))

def f(x_, a_):
    return ((x_ & 52 != 0) and (x_ & 48 == 0)) <= (x_ & a_ != 0)


for a in range(10):
    flag = True
    for x in range(10000):
        if not f(x, a):
            flag = False
            break
    if flag:
        print(a)