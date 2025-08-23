def print_log(f):
    print('x y z w')
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                for w in (0, 1):
                    if f(x, y, z, w):
                        print(x, y, z, w)


def f1(x, y, z, w):
    return ((x and y) == (not z)) and (x and w)

def f3(x, y, z, w):
    return ((x and y) == (not z)) and (x <= w)

def f4(x, y, z, w):
    return ((x and y) == (not z)) and (x or w)


print_log(f1)
print()
print_log(lambda a, b, c, d: ((a and b) == (not c)) and (a == d))
print()
print_log(f3)
print()
print_log(f4)



