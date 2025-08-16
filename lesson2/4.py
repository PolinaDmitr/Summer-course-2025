l = [1, 2, 1, 3, 4, 3, 3, 5]
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)

l3 = list(set(l))
print(l3)

m1 = []
m2 = []
m3 = []
for i in range(1, 11):
    m1.append(i)
    m2.append(i * i)
    m3.append(i ** 3)
print(m1, m2, m3)

k = 0
for i in range(1000, 5001):
    if i % 3 == 0 and i % 5 != 0:
        k += 1
print(k)