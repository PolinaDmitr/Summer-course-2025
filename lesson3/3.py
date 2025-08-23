print('x y z w | f1 f2')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f1 = int((w == x) and (y <= z))
                f2 = int((w <= x) <= (y == z))
                if f1 >= f2:
                    print(x, y, z, w, '|', f1, f2)