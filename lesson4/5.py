a = True
P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
x_valid = []
for x in range(100):
    p = x in P
    q = x in Q
    if (a <= p) and ((not q) <= (not a)):
        x_valid.append(x)
print(x_valid)

A = {6, 12, 18}
for x in range(100):
    p = x in P
    q = x in Q
    a = x in A
    if not (a <= p) and ((not q) <= (not a)):
        print(x)