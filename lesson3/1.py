print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if (w <= y) == (x and z):
                    print(x, y, z, w)
print()
print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if not(not x or not y or not z or w):
                    print(x, y, z, w)
print()
print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if (z or w) and y and x:
                    print(x, y, z, w)